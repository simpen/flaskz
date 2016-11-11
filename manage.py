#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role, Permission, Post, Follow
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)  # 初始化Flask-Migrate


# 为shell命令添加一个上下文，自动把 app,db,User,Role 导入到 python shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post,
                Permission=Permission, Follow=Follow)
manager.add_command("shell", Shell(make_context=make_shell_context))
# 导出数据库迁移命令，通过Flask-Script命令操作数据库迁移
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
