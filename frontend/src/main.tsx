import * as React from "react";
import ReactDOM from "react-dom/client";
import {
  RootRoute,
  Route,
  Router,
  RouterProvider,
} from "@tanstack/react-router";
import { IndexPage } from "@/pages";
import { ContactsPage } from "@/pages/contacts";
import { Layout } from "@/components/layout";
import "@/index.css";

const rootRoute = new RootRoute({
  component: Layout,
});

const indexRoute = new Route({
  getParentRoute: () => rootRoute,
  path: "/",
  component: IndexPage,
});

const contactsRoute = new Route({
  getParentRoute: () => rootRoute,
  path: "/contacts",
  component: ContactsPage,
});

const routeTree = rootRoute.addChildren([indexRoute, contactsRoute]);

const router = new Router({ routeTree });

declare module "@tanstack/react-router" {
  interface Register {
    router: typeof router;
  }
}

const rootElement = document.getElementById("root")!;

if (!rootElement.innerHTML) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>,
  );
}
