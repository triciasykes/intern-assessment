import { ContactCard } from "@/components/contact-card";
import { Contact } from "@/types";
import * as React from "react";

export function ContactsPage() {
  const [contacts, setContacts] = React.useState<Contact[]>();

  React.useEffect(() => {
    async function getContacts() {
      const res = await fetch("http://localhost:5000/contacts");
      const data = await res.json();

      console.log(data);
      setContacts(data);
    }

    getContacts();
  }, []);

  return (
    <>
      <h1 className="font-bold text-3xl text-indigo-600 mb-12">
        Contacts
      </h1>

      <div className="grid grid-cols-4 gap-6">
        {contacts?.map((item) => <ContactCard {...item} />)}
      </div>
    </>
  );
}
