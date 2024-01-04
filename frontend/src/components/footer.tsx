import { Facebook, Instagram, Linkedin, LucideIcon } from "lucide-react";

interface Social {
  icon: LucideIcon;
  href: string;
}

const socials: Social[] = [
  {
    icon: Facebook,
    href: "https://www.facebook.com/zoeeapp",
  },
  {
    icon: Instagram,
    href: "https://www.instagram.com/zoeeapp/",
  },
  {
    icon: Linkedin,
    href: "https://www.linkedin.com/company/zoee/mycompany/",
  },
];

export function Footer() {
  return (
    <footer className="border border-top border-neutral-200">
      <div className="container p-6 flex items-center justify-between">
        <p className="text-sm text-neutral-600">
          Zoee, Inc.<br />
          © 2022 All Rights Reserved Zoee, Inc.
        </p>

        <div className="flex gap-6">
          {socials.map((item) => (
            <a
              href={item.href}
              target="_blank"
              rel="noopener noreferrer"
              className="text-neutral-400 hover:text-indigo-600 transition-colors"
            >
              {<item.icon />}
            </a>
          ))}
        </div>
      </div>
    </footer>
  );
}
