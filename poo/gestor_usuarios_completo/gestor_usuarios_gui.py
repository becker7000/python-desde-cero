
"""
gestor_usuarios_gui.py
Interfaz gráfica (Tkinter) para el proyecto "gestor-usuarios".
Funciones incluidas:
 - Registrar cliente (con tarjeta opcional)
 - Iniciar sesión (login)
 - Listar usuarios
 - Editar usuario
 - Eliminar usuario
 - Exportar/Importar JSON
Requisitos: Python 3.8+, Tkinter (incluido en la mayoría de instalaciones de Python).
Coloca este archivo en la raíz del proyecto (junto a usuarios.json) y ejecútalo:
    python gestor_usuarios_gui.py
"""
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog

RUTA_JSON = "usuarios.json"

class Usuario:
    def __init__(self,nombre,apellido_paterno,apellido_materno,edad,nickname,password,correo,celular):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = int(edad) if edad is not None and str(edad).strip()!='' else None
        self.nickname = nickname
        self.password = password
        self.correo = correo
        self.celular = celular

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "edad": self.edad,
            "nickname": self.nickname,
            "password": self.password,
            "correo": self.correo,
            "celular": self.celular
        }

    @staticmethod
    def from_dict(d):
        return Usuario(
            nombre=d.get("nombre",""),
            apellido_paterno=d.get("apellido_paterno",""),
            apellido_materno=d.get("apellido_materno",""),
            edad=d.get("edad",None),
            nickname=d.get("nickname",""),
            password=d.get("password",""),
            correo=d.get("correo",""),
            celular=d.get("celular","")
        )

class Cliente(Usuario):
    def __init__(self,nombre,apellido_paterno,apellido_materno,edad,nickname,password,correo,celular,tarjeta16Digitos=""):
        super().__init__(nombre,apellido_paterno,apellido_materno,edad,nickname,password,correo,celular)
        self.tarjeta16Digitos = tarjeta16Digitos

    def to_dict(self):
        d = super().to_dict()
        d["tarjeta16Digitos"] = self.tarjeta16Digitos
        return d

    @staticmethod
    def from_dict(d):
        return Cliente(
            nombre=d.get("nombre",""),
            apellido_paterno=d.get("apellido_paterno",""),
            apellido_materno=d.get("apellido_materno",""),
            edad=d.get("edad",None),
            nickname=d.get("nickname",""),
            password=d.get("password",""),
            correo=d.get("correo",""),
            celular=d.get("celular",""),
            tarjeta16Digitos=d.get("tarjeta16Digitos","")
        )

# --- JSON helpers ---
def cargar_usuarios():
    if not os.path.exists(RUTA_JSON):
        return []
    with open(RUTA_JSON,"r",encoding="utf-8") as f:
        try:
            datos = json.load(f)
        except Exception:
            return []
    usuarios=[]
    for d in datos:
        # detecta si tiene tarjeta -> Cliente
        if "tarjeta16Digitos" in d:
            usuarios.append(Cliente.from_dict(d))
        else:
            usuarios.append(Usuario.from_dict(d))
    return usuarios

def guardar_usuarios(lista_usuarios):
    datos = [u.to_dict() for u in lista_usuarios]
    with open(RUTA_JSON,"w",encoding="utf-8") as f:
        json.dump(datos,f,indent=4,ensure_ascii=False)

def registrar_usuario(usuario):
    usuarios = cargar_usuarios()
    for u in usuarios:
        if u.nickname == usuario.nickname:
            return False
    usuarios.append(usuario)
    guardar_usuarios(usuarios)
    return True

def iniciar_sesion(nickname,password):
    usuarios = cargar_usuarios()
    for u in usuarios:
        if u.nickname == nickname and u.password == password:
            return u
    return None

# --- GUI ---
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Usuarios - GUI")
        self.geometry("900x550")
        self.resizable(True,True)

        # Frames
        self.left = ttk.Frame(self, padding=10)
        self.left.pack(side="left", fill="y")
        self.right = ttk.Frame(self, padding=10)
        self.right.pack(side="right", fill="both", expand=True)

        # Left controls
        ttk.Label(self.left, text="Acciones", font=("Segoe UI",14,"bold")).pack(pady=(0,10))
        ttk.Button(self.left, text="Nuevo Usuario", command=self.nuevo_usuario).pack(fill="x", pady=4)
        ttk.Button(self.left, text="Iniciar Sesión", command=self.login_dialog).pack(fill="x", pady=4)
        ttk.Button(self.left, text="Editar seleccionado", command=self.editar_seleccion).pack(fill="x", pady=4)
        ttk.Button(self.left, text="Eliminar seleccionado", command=self.eliminar_seleccion).pack(fill="x", pady=4)
        ttk.Button(self.left, text="Importar JSON...", command=self.importar_json).pack(fill="x", pady=4)
        ttk.Button(self.left, text="Exportar JSON...", command=self.exportar_json).pack(fill="x", pady=4)
        ttk.Button(self.left, text="Refrescar lista", command=self.refresh_lista).pack(fill="x", pady=4)
        ttk.Button(self.left, text="Salir", command=self.quit).pack(fill="x", pady=12)

        # Search box
        ttk.Label(self.left, text="Buscar (nickname o nombre)").pack(pady=(10,0))
        self.busqueda_var = tk.StringVar()
        ent = ttk.Entry(self.left, textvariable=self.busqueda_var)
        ent.pack(fill="x", pady=4)
        ent.bind("<Return>", lambda e: self.refresh_lista())
        ttk.Button(self.left, text="Buscar", command=self.refresh_lista).pack(fill="x", pady=4)

        # Right: Treeview of users
        columns = ("nickname","nombre","correo","celular","edad","tarjeta")
        self.tree = ttk.Treeview(self.right, columns=columns, show="headings", selectmode="browse")
        headings = {
            "nickname":"Nickname",
            "nombre":"Nombre completo",
            "correo":"Correo",
            "celular":"Celular",
            "edad":"Edad",
            "tarjeta":"Tarjeta (si aplica)"
        }
        for c in columns:
            self.tree.heading(c, text=headings[c])
            self.tree.column(c, width=120, anchor="w")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<Double-1>", lambda e: self.ver_detalle())

        # Status
        self.status_var = tk.StringVar()
        ttk.Label(self.right, textvariable=self.status_var).pack(anchor="w", pady=(6,0))

        self.refresh_lista()

    def refresh_lista(self):
        q = self.busqueda_var.get().strip().lower()
        usuarios = cargar_usuarios()
        # clear
        for i in self.tree.get_children():
            self.tree.delete(i)
        count=0
        for u in usuarios:
            if q:
                if q not in u.nickname.lower() and q not in u.nombre.lower():
                    continue
            tarjeta = getattr(u,"tarjeta16Digitos", "")
            nombre_completo = f"{u.nombre} {u.apellido_paterno} {u.apellido_materno}".strip()
            edad = u.edad if u.edad is not None else ""
            self.tree.insert("", "end", values=(u.nickname, nombre_completo, u.correo, u.celular, edad, tarjeta))
            count+=1
        self.status_var.set(f"Usuarios mostrados: {count}")

    def nuevo_usuario(self):
        dlg = UsuarioDialog(self, title="Registrar nuevo usuario")
        self.wait_window(dlg)
        if dlg.result:
            data = dlg.result
            if data.get("es_cliente"):
                usuario = Cliente.from_dict(data)
            else:
                usuario = Usuario.from_dict(data)
            if registrar_usuario(usuario):
                messagebox.showinfo("Registro", "Usuario registrado correctamente.")
                self.refresh_lista()
            else:
                messagebox.showwarning("Registro", "El nickname ya existe. Elija otro.")

    def login_dialog(self):
        dlg = LoginDialog(self)
        self.wait_window(dlg)
        if dlg.result:
            nickname,password = dlg.result
            usuario = iniciar_sesion(nickname,password)
            if usuario:
                messagebox.showinfo("Login correcto", f"Bienvenido {usuario.nombre} ({usuario.nickname})")
            else:
                messagebox.showerror("Login fallido", "Nickname o contraseña incorrectos.")

    def get_selected_nickname(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Seleccionar", "Seleccione un usuario de la lista.")
            return None
        return self.tree.item(sel[0],"values")[0]

    def editar_seleccion(self):
        nick = self.get_selected_nickname()
        if not nick: return
        usuarios = cargar_usuarios()
        usr = next((u for u in usuarios if u.nickname==nick),None)
        if not usr:
            messagebox.showerror("Error","Usuario no encontrado.")
            self.refresh_lista()
            return
        initial = usr.to_dict()
        if isinstance(usr, Cliente):
            initial["es_cliente"]=True
        dlg = UsuarioDialog(self, title="Editar usuario", initial=initial)
        self.wait_window(dlg)
        if dlg.result:
            data = dlg.result
            # update object
            if data.get("es_cliente"):
                nuevo = Cliente.from_dict(data)
            else:
                nuevo = Usuario.from_dict(data)
            # replace in list
            usuarios = [u for u in usuarios if u.nickname!=nick]
            usuarios.append(nuevo)
            guardar_usuarios(usuarios)
            messagebox.showinfo("Editar","Usuario actualizado.")
            self.refresh_lista()

    def eliminar_seleccion(self):
        nick = self.get_selected_nickname()
        if not nick: return
        if not messagebox.askyesno("Eliminar","¿Eliminar usuario '%s'?"%nick):
            return
        usuarios = cargar_usuarios()
        usuarios = [u for u in usuarios if u.nickname!=nick]
        guardar_usuarios(usuarios)
        messagebox.showinfo("Eliminar","Usuario eliminado.")
        self.refresh_lista()

    def ver_detalle(self):
        nick = self.get_selected_nickname()
        if not nick: return
        usuarios = cargar_usuarios()
        usr = next((u for u in usuarios if u.nickname==nick),None)
        if not usr:
            messagebox.showerror("Error","Usuario no encontrado.")
            return
        texto = json.dumps(usr.to_dict(),indent=4,ensure_ascii=False)
        DetailDialog(self, title=f"Detalle: {nick}", text=texto)

    def importar_json(self):
        path = filedialog.askopenfilename(title="Seleccionar archivo JSON", filetypes=[("JSON files","*.json"),("All files","*.*")])
        if not path: return
        try:
            with open(path,"r",encoding="utf-8") as f:
                datos = json.load(f)
            # validates that each entry has nickname
            usuarios=[]
            for d in datos:
                if "nickname" not in d:
                    continue
                if "tarjeta16Digitos" in d:
                    usuarios.append(Cliente.from_dict(d))
                else:
                    usuarios.append(Usuario.from_dict(d))
            guardar_usuarios(usuarios)
            messagebox.showinfo("Importar","Importación exitosa. Reemplazó usuarios existentes.")
            self.refresh_lista()
        except Exception as e:
            messagebox.showerror("Error al importar", str(e))

    def exportar_json(self):
        path = filedialog.asksaveasfilename(title="Exportar usuarios a...", defaultextension=".json", filetypes=[("JSON files","*.json")])
        if not path: return
        usuarios = cargar_usuarios()
        datos = [u.to_dict() for u in usuarios]
        try:
            with open(path,"w",encoding="utf-8") as f:
                json.dump(datos,f,indent=4,ensure_ascii=False)
            messagebox.showinfo("Exportar","Exportación completada.")
        except Exception as e:
            messagebox.showerror("Error al exportar", str(e))

class UsuarioDialog(tk.Toplevel):
    def __init__(self, parent, title="Usuario", initial=None):
        super().__init__(parent)
        self.title(title)
        self.resizable(False,False)
        self.result = None
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill="both", expand=True)
        entries = {}
        fields = [
            ("nickname","Nickname"),
            ("password","Password"),
            ("nombre","Nombre"),
            ("apellido_paterno","Apellido paterno"),
            ("apellido_materno","Apellido materno"),
            ("edad","Edad"),
            ("correo","Correo"),
            ("celular","Celular"),
            ("tarjeta16Digitos","Tarjeta 16 dígitos (opcional)"),
        ]
        for key,label in fields:
            ttk.Label(frm, text=label).pack(anchor="w")
            ent = ttk.Entry(frm)
            ent.pack(fill="x", pady=2)
            entries[key]=ent

        self.es_cliente_var = tk.BooleanVar(value=False)
        chk = ttk.Checkbutton(frm, text="Guardar como Cliente (incluye tarjeta)", variable=self.es_cliente_var)
        chk.pack(anchor="w", pady=6)

        btnfrm = ttk.Frame(frm)
        btnfrm.pack(fill="x", pady=6)
        ttk.Button(btnfrm, text="Cancelar", command=self.cancel).pack(side="right", padx=4)
        ttk.Button(btnfrm, text="Guardar", command=lambda:self.guardar(entries)).pack(side="right")

        # Prefill if editing
        if initial:
            for k,v in initial.items():
                if k in entries:
                    entries[k].insert(0,str(v))
            if initial.get("tarjeta16Digitos"):
                self.es_cliente_var.set(True)
        self.entries=entries

    def guardar(self, entries):
        data = {k:entries[k].get().strip() for k in entries}
        if not data["nickname"] or not data["password"] or not data["nombre"]:
            messagebox.showwarning("Validación","Nickname, password y nombre son obligatorios.")
            return
        data["es_cliente"] = self.es_cliente_var.get()
        # edad may be empty
        try:
            data["edad"] = int(data["edad"]) if data["edad"]!='' else None
        except ValueError:
            messagebox.showwarning("Validación","Edad debe ser un número.")
            return
        self.result = data
        self.destroy()

    def cancel(self):
        self.result = None
        self.destroy()

class LoginDialog(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.title("Iniciar sesión")
        self.resizable(False,False)
        frm = ttk.Frame(self,padding=12)
        frm.pack(fill="both",expand=True)
        ttk.Label(frm,text="Nickname").pack(anchor="w")
        self.nick = ttk.Entry(frm)
        self.nick.pack(fill="x",pady=4)
        ttk.Label(frm,text="Password").pack(anchor="w")
        self.passw = ttk.Entry(frm, show="*")
        self.passw.pack(fill="x",pady=4)
        btnfrm = ttk.Frame(frm)
        btnfrm.pack(fill="x", pady=6)
        ttk.Button(btnfrm,text="Cancelar", command=self.cancel).pack(side="right", padx=4)
        ttk.Button(btnfrm,text="Entrar", command=self.entrar).pack(side="right")
        self.result=None

    def entrar(self):
        nick = self.nick.get().strip()
        pw = self.passw.get().strip()
        if not nick or not pw:
            messagebox.showwarning("Validación","Complete nickname y password.")
            return
        self.result = (nick,pw)
        self.destroy()

    def cancel(self):
        self.result=None
        self.destroy()

class DetailDialog(tk.Toplevel):
    def __init__(self,parent,title="Detalle",text=""):
        super().__init__(parent)
        self.title(title)
        self.geometry("600x400")
        txt = tk.Text(self, wrap="word")
        txt.pack(fill="both",expand=True)
        txt.insert("1.0", text)
        txt.configure(state="disabled")

if __name__ == "__main__":
    app = App()
    app.mainloop()
