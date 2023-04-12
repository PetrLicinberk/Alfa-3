import mysql.connector as mysql
import sys, getopt, config
import view, controller, model

def main(args):
    conf = config.Config()
    conf.set_config_file('config/default.ini')
    options, arguments = getopt.getopt(args, 'c:')
    for opt, arg in options:
        if opt == '-c':
            conf.set_config_file(arg)
    conf.read()

    try:
        conn = mysql.connect(host=conf['database']['host'], user=conf['database']['user'], password=conf['database']['password'])
    except:
        print('Pripojeni k databazi selhalo.')
        exit()
    v = view.View()
    c = controller.Controller()
    m = model.Model(conn, conf)

    v._controller = c
    v._model = m
    c._view = v
    c._model = m
    m._controller = c
    m._view = v

    try:
        c.run()
    except KeyboardInterrupt:
        print('\nProgram ukoncen.')
    conn.close()


if __name__ == '__main__':
    main(sys.argv[1:])