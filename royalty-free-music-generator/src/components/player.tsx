// Player.jsx
import AudioPlayer from "react-h5-audio-player";
import "react-h5-audio-player/lib/styles.css";

const Player = ({ url }) => {
  return (
    <div className="fixed bottom-0 right-0 z-50 w-[1261px]">
      {" "}
      {/* Tailwind classes for sticky positioning */}
      {url && (
        <AudioPlayer
          className="w-full" // Tailwind class for full width
          autoPlay
          src={url}
          onPlay={(e) => console.log("onPlay")}
          // other props here
        />
      )}
    </div>
  );
};

export default Player;
