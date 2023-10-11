from tortoise import Tortoise, fields
from tortoise.models import Model
import asyncio

# Define el modelo de tu tabla, por ejemplo, una tabla de usuarios
class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100)

    def __str__(self):
        return self.username

# Función asincrónica para ejecutar operaciones CRUD
async def run():
    # Conecta a la base de datos
    await Tortoise.init(
        db_url='postgres://username:password@localhost/mydatabase',
        modules={'models': ['__main__']}
    )

    # Crea la tabla en la base de datos
    await Tortoise.generate_schemas()

    while True:
        print("\n1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Obtener usuario por ID")
        print("4. Eliminar usuario por ID")
        print("5. Salir")

        choice = input("\nElige una opción: ")

        if choice == "1":
            username = input("Ingresa el nombre de usuario: ")
            email = input("Ingresa el email: ")
            user = await User.create(username=username, email=email)
            print(f"Usuario {user} creado con éxito.")

        elif choice == "2":
            users = await User.all()
            for user in users:
                print(user)

        elif choice == "3":
            user_id = int(input("Ingresa el ID del usuario: "))
            user = await User.get(id=user_id)
            print(user)

        elif choice == "4":
            user_id = int(input("Ingresa el ID del usuario: "))
            user = await User.get(id=user_id)
            await user.delete()
            print(f"Usuario {user} eliminado con éxito.")

        elif choice == "5":
            break

        else:
            print("Opción no válida.")

# Ejecuta la función asincrónica
loop = asyncio.get_event_loop()
loop.run_until_complete(run())