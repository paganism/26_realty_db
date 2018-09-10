from app import create_app, db
from app.models import Ads


app = create_app()
print(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Ads': Ads}
