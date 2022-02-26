This project estimates the "fanbase development speed" of Bandori and Love Live! by approximating the cummulative sum of *official* video view count in each month from 12/2011 to 11/2021, then build a linear regression model to make predictions until 2031.

Notebooks: 
- scrape.ipynb: use YouTube API v3 to get the information of all videos given in the list below. 
- plotting.ipynb: draw plots.

Video sources:
- **Love Live!**: [Love Live! Official Channel](https://www.youtube.com/c/lovelive_series), [μ's Playlist on Lantis channel](https://www.youtube.com/watch?v=HQYtGvXGGJA&list=PLmgGL3shzkGM9akfMoobnVhE3XCP42lHb), [Aqours Playlist on Lantis channel](https://www.youtube.com/watch?v=sMZ7iIxIJ6o&list=PLmgGL3shzkGM96YqVhygd3Skb42CTa-hy), [Nijigasaki Livestream Channel](https://www.youtube.com/channel/UCWTbUllFchDX1IxfJF-N0UA).
- **Bandori**: [Japanese Bandori Channel](https://www.youtube.com/channel/UCN-bFIdJM0gQlgX7h6LKcZA), [Global Bandori Channel](https://www.youtube.com/c/BanGDreamGirlsBandParty).
