import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Slider } from "@/components/ui/slider";
import { Input } from "@/components/ui/input";
import { AspectRatio } from "@/components/ui/aspect-ratio";
import defaultImage from "./../assets/dashboard/default-image.png";
import toast from "react-hot-toast"; // Import toast for showing messages
import Loader from "@/components/ui/loader";
import { useOutletContext, useNavigate } from "react-router-dom";
import lockSvg from "./../assets/dashboard/lock.svg";
const CreateImage = () => {
  const context = useOutletContext() as any; // Cast the context to 'any'

  const { isLoggedIn, setCurrentSong, currentSong } = context; // Now you can destructure without TypeScript errors
  const navigate = useNavigate();
  const [sliderValue, setSliderValue] = useState(33);
  const [imagePreview, setImagePreview] = useState(defaultImage);
  const [loading, setLoading] = useState(false); // Loading state

  // Function to handle the change event of the slider
  const handleSliderChange = (bpm) => {
    setSliderValue(bpm);
  };

  // Function to handle the change event of the file input
  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file && file.type.startsWith("image")) {
      // Create a URL for the image to display as a preview
      const reader = new FileReader();
      reader.onloadend = () => {
        if (typeof reader.result === "string") {
          setImagePreview(reader.result);
        }
      };
      reader.readAsDataURL(file);
    } else {
      setImagePreview(null);
    }
  };
  const handleGenerate = () => {
    if (!imagePreview || imagePreview === defaultImage) {
      toast.error("Please upload an image");
      return;
    }

    if (!sliderValue) {
      toast.error("Please select a duration");
      return;
    }

    const payload = {
      token: localStorage.getItem("authToken"),
      private: 0,
      image: imagePreview,
      duration: sliderValue,
    };

    console.log(
      "Generating tune with the following data:",
      JSON.stringify(payload)
    );

    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      // Simulate setting a song after generation, you might want to change this to a real function call
      console.log("Tune generated successfully!");
      setCurrentSong(
        "https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3"
      );
    }, 3000);
  };

  useEffect(() => {
    // Effect to handle when imagePreview changes, e.g., for sending to a server
    // Convert imagePreview back to file or use imageFile to send to server
    console.log(imagePreview);
  }, [imagePreview]);
  return (
    <div>
      {isLoggedIn ? (
        <>
          {" "}
          <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
            Inspire
          </h1>
          <p className="text-md mt-2 text-muted-foreground">
            Transform the essence of your images into unique AI-generated tunes.
            Let our advanced AI analyze<br></br> the mood, colors and elements
            of your image to compose the perfect background music <br></br>that
            complements your visual content.
          </p>
          <div className="flex flex-col">
            <h3 className="mt-8 scroll-m-20 text-xl font-semibold tracking-tight">
              1. Upload your image
            </h3>
            <div className="grid w-full max-w-lg items-center gap-1.5 ">
              {imagePreview && (
                <div className="mt-4">
                  <img
                    src={imagePreview}
                    alt="Image preview"
                    style={{ width: "100%", height: "auto" }}
                    className="rounded-md"
                  />
                </div>
              )}
              <Input id="picture" type="file" onChange={handleImageChange} />

              <div className="mt-4"></div>
            </div>
            <h3 className="mt-8 scroll-m-20 text-xl font-semibold tracking-tight">
              2. Set your duration
            </h3>
            <div className="mt-4 inline-block w-72">
              <Slider
                onValueChange={handleSliderChange}
                defaultValue={[33]}
                max={100}
                step={1}
              />
              <p className="text-sm mt-2 text-muted-foreground">
                {sliderValue} seconds
              </p>
            </div>

            <Button
              className="mt-8 bg-purple-700 flex items-center justify-center"
              variant="default"
              onClick={handleGenerate}
            >
              {loading ? <Loader /> : "Generate"}
            </Button>
          </div>
        </>
      ) : (
        <div className="flex h-screen w-[1200px] flex-col items-center justify-center bg-white rounded-lg">
          <img src={lockSvg} alt="lock" className="w-20 mb-4" />
          <h2 className="mb-4 text-2xl font-semibold text-gray-800">
            Vibes are best if you're logged in
          </h2>
          <p className="mb-8 text-md text-gray-600">
            Please login to access this page.
          </p>
          <Button
            className="bg-purple-700 text-white font-bold py-2 px-4 rounded hover:bg-purple-800"
            onClick={() => navigate("/login")}
          >
            Login
          </Button>
        </div>
      )}
    </div>
  );
};
export default CreateImage;
