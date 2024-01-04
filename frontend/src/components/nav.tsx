import * as React from "react";
import zoeeLogo from "@/assets/logo.svg";
import { Link } from "@tanstack/react-router";
import { User } from "@/types";

export function Nav() {
  const [user, setUser] = React.useState<User>();

  React.useEffect(() => {
    async function getUser() {
      const res = await fetch("http://localhost:5000/user");
      const data = await res.json();

      console.log(data);
      setUser(data);
    }

    getUser();
  }, []);

  const linkClasses =
    "px-3 py-1.5 rounded-lg font-medium text-neutral-500 hover:bg-neutral-100 [&.active]:text-indigo-600 transition-colors";

  return (
    <nav className="container mt-3">
      <div className="bg-white rounded-xl shadow-lg py-4 px-6 flex items-center justify-between">
        <img src={zoeeLogo} alt="Zoee logo" />

        <div className="flex gap-3">
          <Link to="/" className={linkClasses}>
            Home
          </Link>
          <Link to="/contacts" className={linkClasses}>
            Contacts
          </Link>
        </div>

        {/* Add user icon here */}
        <div className="rounded-full bg-indigo-600 w-10 h-10 flex items-center justify-center text-white text-lg">
          {user?.first_name[0]}
        </div>
      </div>
    </nav>
  );
}
