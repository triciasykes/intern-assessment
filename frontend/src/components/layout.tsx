import { Outlet } from "@tanstack/react-router";
import { Nav } from "@/components/nav";
import { Footer } from "@/components/footer";

export function Layout() {
  return (
    <>
      <Nav />
      <main className="flex-1 flex flex-col justify-center container my-12">
        <Outlet />
      </main>
      <Footer />
    </>
  );
}
