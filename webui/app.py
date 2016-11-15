from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
from webui.views import app as webui

app = DispatcherMiddleware(None, {
    '/webui': webui
})

if __name__ == '__main__':
    run_simple('127.0.0.1', 5000, app, use_reloader=False, use_debugger=False, use_evalex=False)
