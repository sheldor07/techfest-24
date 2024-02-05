import { ReactNode } from "react";
import { RouteObject } from "react-router";
import Dashboard from "./pages/Dashboard";
import Landing from "./pages/Landing";
import Explore from "./pages/Explore";
import Library from "./pages/Library";
import CreateText from "./pages/CreateText";
import Signup from "./pages/Signup";
import Login from "./pages/Login";
import ErrorPage from "./pages/ErrorPage";
import CreateImage from "./pages/CreateImage";

export const routes: RouteObject[] = [
  {
    path: "/",
    element: <Dashboard />,
  },
  {
    path: "/dashboard",
    element: <Dashboard />,
    children: [
      {
        path: "explore",
        element: <Explore />,
      },
      {
        path: "library",
        element: <Library />,
      },
      {
        path: "create-text",
        element: <CreateText />,
      },
      {
        path: "create-image",
        element: <CreateImage />,
      },
    ],
  },
  {
    path: "/signup",
    element: <Signup />,
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "*",
    element: <ErrorPage />,
  },
];
