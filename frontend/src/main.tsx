import * as React from "react";
import ReactDOM from "react-dom/client";
import {
  Outlet,
  RootRoute,
  Route,
  Router,
  RouterProvider,
} from "@tanstack/react-router";
import "@/index.css";
import { IndexPage } from "@/pages";
import { ContactsPage } from "@/pages/contacts";
import { Nav } from "@/components/nav";
import { Footer } from "@/components/footer";

const rootRoute = new RootRoute({
  component: () => (
    <>
      <Nav />
      <main className="flex-1 flex flex-col justify-center container my-12">
        <Outlet />
      </main>
      <Footer />
    </>
  ),
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
