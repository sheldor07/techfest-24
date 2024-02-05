export default function ErrorPage() {
  return (
    <div className="flex flex-col justify-center items-center h-screen bg-gray-50 text-gray-800">
      <div className="p-6 max-w-md w-full rounded-lg shadow-md bg-white">
        <div className="text-6xl font-bold text-red-500">404</div>
        <div className="mt-2 text-xl font-semibold">Page Not Found</div>
        <div className="mt-2">
          The page you are looking for doesn't exist or an other error occurred.
          Go back, or head over to the home page to choose a new direction.
        </div>
        <a
          href="/dashboard/explore"
          className="mt-4 inline-block px-6 py-2 text-sm font-medium leading-6 text-center text-white uppercase transition bg-red-500 rounded shadow ripple hover:shadow-lg hover:bg-red-600 focus:outline-none"
        >
          Back to Home
        </a>
      </div>
    </div>
  );
}
