import input_
import import_
import export_


def start():
    if input_.mode() == '1':
        if input_.form() == '1':
            info = input_.exp()
            export_.export_func1(info)
        else:
            info = input_.exp()
            export_.export_func2(info)

    else:
        if input_.form() == '1':
            info = input_.imp()
            import_.import_func1(info)
        else:
            info = input_.imp()
            import_.import_func2(info)
