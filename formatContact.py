import vobject

# Ruta al archivo vCard
path_to_vcf = 'contactos.vcf'

# Función para leer los contactos de un archivo vCard
def read_vcards(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        vcards = vobject.readComponents(file)
        contacts = []
        for vcard in vcards:
            contact = {}
            if hasattr(vcard, 'n'):
                # Accedemos directamente a los componentes del objeto Name
                name_components = vcard.n.value
                # Construimos el nombre completo usando los componentes disponibles
                full_name = " ".join(filter(None, [name_components.family, name_components.given, 
                                                   name_components.additional, name_components.prefix,
                                                   name_components.suffix]))
                contact['name'] = full_name.strip()
            if hasattr(vcard, 'tel'):
                contact['phone'] = vcard.tel.value.strip().replace(' ', '').replace('-', '')
            if contact:
                contacts.append(contact)
        return contacts


# Leer los contactos del archivo vCard
contacts = read_vcards(path_to_vcf)

# Guardar los contactos en un archivo de texto
with open('contactos_exportados.txt', 'w', encoding='utf-8') as file:
    for contact in contacts:
        file.write(f"Nombre: {contact.get('name', 'Sin Nombre')} - Teléfono: {contact.get('phone', 'Sin Teléfono')}\n")

print("Contactos guardados en 'contactos_exportados.txt'.")


# Filtro contactos que tengan nombre vacío
filtered_contacts = [contact for contact in contacts if 'name' in contact and contact['name'].strip()]

# Filtro contactos que tengan número de teléfono de menos de 8 caracteres
filtered_contacts = [contact for contact in filtered_contacts if 'phone' in contact and len(contact['phone'].replace(' ', '').replace('-', '')) >= 8]

# Imprimir los contactos filtrados
print(filtered_contacts)

print("\n \n \n \n \n \n")
# Imprimir cantidad total de contactos

print("Número total de contactos procesados:", len(contacts))
