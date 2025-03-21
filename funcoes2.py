def loginUsuario(perfil):

    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')


loginUsuario('Admin')     # Testando com 'Admin'
loginUsuario('admin')     # Testando com 'admin'
loginUsuario('User')      # Testando com 'User'
loginUsuario('usuário')