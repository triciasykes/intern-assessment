import { Contact } from "@/types";

export function ContactCard(props: Contact) {
  return (
    <div className="bg-neutral-200/50 rounded-2xl h-64 flex flex-col items-center justify-center gap-2">
      <img src={props.avatar} alt="profile pic" className="rounded-full" />
      <h2 className="font-semibold text-lg">
        {props.first_name} {props.last_name}
      </h2>
      <h3 className="text-neutral-600">{props.email}</h3>
    </div>
  );
}
