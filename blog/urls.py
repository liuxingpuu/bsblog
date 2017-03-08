from controllers import main
from controllers import auth

routers = {
    (main.main, ''),
    (auth.auth, '/auth')
}