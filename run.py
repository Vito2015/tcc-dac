# coding: utf-8
"""
    tcc-dac.run
    ~~~~~~~~~~~~~~~

    tcc-dac website test run module.
    :copyright: (c) 2015 by Vito.
    :license: GNU, see LICENSE for more details.
"""
from dac.app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', 8080, debug=True)
