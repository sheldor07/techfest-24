const options = {
  uri: "https://1agnfox1re.execute-api.ap-south-1.amazonaws.com/Production/techfest_signup",
  method: "POST",
  headers: {
    host: "localhost:3001",
    connection: "keep-alive",
    "content-length": "57",
    "sec-ch-ua":
      '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "content-type": "application/json",
    dnt: "1",
    "sec-ch-ua-mobile": "?0",
    "user-agent":
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "x-api-key": "2RttSEJUCC4f3s9K4FO8A2LQhcxzcyZy8ENOzYEV",
    "sec-ch-ua-platform": '"macOS"',
    accept: "*/*",
    origin: "http://localhost:5173",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    referer: "http://localhost:5173/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
  },
  body: '{"email":"yajatgulati01@gmail.com","password":"testtest"}',
};
try {
  const r = fetch(
    "https://1agnfox1re.execute-api.ap-south-1.amazonaws.com/Production/techfest_signup",
    options
  );

  console.log(r);
} catch (err) {
  console.log(err);
}
