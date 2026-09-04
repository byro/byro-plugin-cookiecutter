from setuptools import setup
from setuptools.command.build_py import build_py


class CustomBuild(build_py):
    """Compile translations when building in an environment that has Django.

    Isolated builds (plain ``pip install`` / ``python -m build``) have no Django
    available; they ship the ``.po`` sources only. byro's
    ``install_local_plugins.sh`` installs with ``--no-build-isolation`` so the
    ``.mo`` files are generated there.
    """

    def run(self):
        try:
            from django.core import management
        except ModuleNotFoundError:
            pass
        else:
            management.call_command("compilemessages", verbosity=1)
        super().run()


setup(cmdclass={"build_py": CustomBuild})
