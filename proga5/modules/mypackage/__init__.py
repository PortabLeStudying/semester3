# Этот код выполняется при `import mypackage`
print("mypackage.__init__ выполнен")

AUTHOR = "PortabLe"

def package_info():
    return f"Пакет mypackage, автор {AUTHOR}"