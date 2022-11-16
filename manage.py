def deploy():
    from Application.app import create_app, database
    from Application.Model import AccountsTable

    app = create_app()
    app.app_context().push()
    database.create_all()

    database.session.commit()


deploy()
