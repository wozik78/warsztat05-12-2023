class ContactList(list['Contact']):
    def search(self,name):
        matching_contacts =[]
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts

contact_list =ContactList()
print(contact_list) #[]
print(type(contact_list)) # class

contact_list.append()