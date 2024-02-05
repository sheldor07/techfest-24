import Player from "@/components/player";
import { Card } from "@/components/ui/card";
import { useState } from "react";
import { useOutletContext } from "react-router-dom";
import downloadSvg from "./../assets/dashboard/download.svg";
const Library = () => {
  const context = useOutletContext() as any; // Cast the context to 'any'
  const { setCurrentSong, currentSong } = context; // Now you can destructure without TypeScript errors
  const generateFilename = (title) => {
    return title.toLowerCase().replace(/\s+/g, "-") + ".wav";
  };
  const songData = [
    {
      id: 1,
      title: "Moonlight Sonata",
      artist: "Ludwig van Beethoven",
      genre: "Classical",
      duration: "5:32",
      url: " https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3",
    },
    {
      id: 2,
      title: "Bohemian Rhapsody",
      artist: "Queen",
      genre: "Rock",
      duration: "5:55",
      url: "https://techfest-mp3.s3.amazonaws.com/AKIAQJOTY2BOENJZM2VT?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQJOTY2BOENJZM2VT%2F20240205%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20240205T214533Z&X-Amz-Expires=36000&X-Amz-SignedHeaders=host&X-Amz-Signature=5de34805fcc0ba658b2891ad913afd44232588226cb8e3b2690e19cbc6553e2b",
    },
    {
      id: 3,
      title: "Smells Like Teen Spirit",
      artist: "Nirvana",
      genre: "Grunge",
      duration: "4:39",
      url: "https://www.example.com/smells-like-teen-spirit",
    },
    {
      id: 4,
      title: "Shallow",
      artist: "Lady Gaga, Bradley Cooper",
      genre: "Pop",
      duration: "3:35",
      url: "https://www.example.com/shallow",
    },
  ];
  const handleSongSelect = (url) => {
    setCurrentSong(url);
    console.log("currentSong", currentSong);
  };

  return (
    <div>
      <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
        Library
      </h1>{" "}
      <p className="text-md mt-2 text-muted-foreground">
        {" "}
        These are the AI-generated tunes that you have created <br></br> and
        saved. You can listen to them anytime, anywhere.
      </p>
      {
        <div className="grid grid-cols-1 gap-1 mt-12">
          {songData.map((song) => (
            <div
              key={song.id}
              className={`flex flex-row p-2 w-[800px] rounded-md ${
                currentSong === song.url
                  ? " bg-purple-200"
                  : "border-transparent"
              }  hover:bg-neutral-200  duration-500 items-center justify-between`}
            >
              <div onClick={() => handleSongSelect(song.url)}>
                <h2 className="text-md font-semibold">{song.title}</h2>
                <p className="text-sm text-muted-foreground">{song.genre}</p>
              </div>
              <div className="flex items-center">
                <p className="text-sm text-muted-foreground mr-4">
                  {song.duration}
                </p>
                <a
                  href={song.url}
                  download={generateFilename(song.title)}
                  className=" text-white font-bold py-1 px-2 rounded inline-flex items-center"
                >
                  <img src={downloadSvg} className="w-5" />
                </a>
              </div>
            </div>
          ))}
        </div>
      }{" "}
    </div>
  );
};
export default Library;
