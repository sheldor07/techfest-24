import { Outlet, Link, redirect } from "react-router-dom";
import { useEffect, useState } from "react";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import linkjson from "../jsondata/link.json";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuPortal,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Button } from "@/components/ui/button";
import { SideBarButton } from "@/components/ui/sidebar-button";
import Player from "./../components/player";

import createSvg from "./../assets/dashboard/create.svg";
import exploreSvg from "./../assets/dashboard/explore.svg";
import librarySvg from "./../assets/dashboard/library.svg";
import imageSvg from "./../assets/dashboard/image.svg";
import { Toaster } from "react-hot-toast";
import { useNavigate } from "react-router-dom";
const Dashboard = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  useEffect(() => {
    if (localStorage.getItem("authToken")) {
      setIsLoggedIn(true);
    }
  }, []);
  const navigate = useNavigate();
  const [currentSong, setCurrentSong] = useState(null);
  const handleLogout = async () => {
    const payload = {
      token: localStorage.getItem("authToken"),
    };

    const response = await fetch(linkjson.link+"/techfest-signout", {
      method: "POST",
      headers: {
        "x-api-key": "SUsY4RKu6h4AGCiYA2BLs9YHxxThZyQv6YawpI6l",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (response.ok) {
      localStorage.removeItem("authToken");
      navigate("/login");
    } else {
      console.log("error in logging out");
    }
  };
  return (
    <div className="flex flex-row pb-24">
      <nav className="flex flex-col items-left justify-between px-4 py-12 mr-10 border-r-2 relative left-0 top-0 h-screen">
        <div>
          {" "}
          <div className="flex items-center   border-b pb-2 tracking-tight  pb-4">
            <div className="hue-radial  "></div>
            <h2 className="scroll-m-20 text-3xl font-semibold first:mt-0">
              Vibes{" "}
            </h2>
          </div>
          <div className="grid grid-cols-1 gap-2 items-center w-36 mt-2">
            <SideBarButton
              variant="ghost"
              onClick={() => navigate("/dashboard/explore")}
            >
              <Link to="/dashboard/explore" className="flex">
                <img src={exploreSvg} alt="explore" className="w-5 mr-2" />
                Explore
              </Link>
            </SideBarButton>
            <SideBarButton
              variant="ghost"
              onClick={() => navigate("/dashboard/create-text")}
            >
              <Link to="/dashboard/create-text" className="flex w-full">
                <img
                  src={createSvg}
                  alt="create"
                  className="w-5 mr-2"
                />
                Create
              </Link>
            </SideBarButton>
            <SideBarButton
              variant="ghost"
              onClick={() => navigate("/dashboard/create-image")}
            >
              <Link to="/dashboard/create-image" className="flex">
                <img
                  src={imageSvg}
                  alt="create"
                  className="w-5 mr-2"
                />
                Inspire
              </Link>
            </SideBarButton>
            <SideBarButton
              variant="ghost"
              onClick={() => navigate("/dashboard/library")}
            >
              <Link to="/dashboard/library" className="flex">
                <img
                  src={librarySvg}
                  alt="library"
                  className="w-5 mr-2"
                />
                Library
              </Link>
            </SideBarButton>
          </div>
        </div>{" "}
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <button className="outline-none">
              <Avatar>
                <AvatarImage src="https://bit.ly/dan-abramov" />
                <AvatarFallback>YA</AvatarFallback>
              </Avatar>
            </button>
          </DropdownMenuTrigger>
          <DropdownMenuContent className="w-48">
            <DropdownMenuLabel>My Account</DropdownMenuLabel>{" "}
            <DropdownMenuItem>
              {isLoggedIn ? (
                <div onClick={handleLogout}>Log out</div>
              ) : (
                <Button asChild>
                  <Link to="/login">Log in</Link>
                </Button>
              )}
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </nav>
      <div className="py-12 px-4 flex justify-right">
        <Outlet context={{ setCurrentSong, currentSong, isLoggedIn }} />
      </div>
      <Player url={currentSong} />
      <Toaster />
    </div>
  );
};
export default Dashboard;
