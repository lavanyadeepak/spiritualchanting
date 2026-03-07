# Spiritual Chanting Tool

## A lightweight (<10MB) JavaScript engine for background chanting. Chant files managed separately.

### Why No Chants Included?

- **Size:** Chant collections (audio files) can exceed 1GB—too large for GitHub.  
- **Flexibility:** Users add their own chants (local files or external URLs).  
- **Legal Safety:** Avoid distributing copyrighted/litigious content.  

### How to Use

1. **Set Up Chants**  
   - Step 1: Download chants (your own or request public-domain suggestions).  
   - Step 2: Store them outside the repo (e.g., `~/my-chants/` or cloud storage).  
   - Step 3: Edit `chants.data.js` (located in `chants/data/`) to point to their paths.  

2. **Run the Engine**  
   - Open `index.html` in a browser (works offline with local files).  
   - For web deployment, host audio files separately (e.g., AWS S3, Dropbox).  

---

### Attribution & Metadata

Each chant entry now includes additional metadata fields for clarity and compliance:

- **textualOrigin:** Historical or scriptural source of the chant.  
- **likelyRecordingSource:** Notes on recording provenance (verify before distribution).  
- **copyrightStatus:** Indicates whether the recording requires verification.  

An **Attribution page** is included to summarize these details for transparency.

---

### Docker Deployment

A Docker image with a built-in web server for playback is available:  
👉 [hub.docker.com/r/lavanyadeepak/byte-shrine](https://hub.docker.com/r/lavanyadeepak/byte-shrine)

Example run command:
```bash
docker run -p 8080:80 lavanyadeepak/byte-shrine
```

### Need Pre-Made Chants?
Contact the maintainer (@lavanyadeepak) for public-domain sources or curated lists.

### Copyrights
Audio files are user-provided. The maintainer makes no claim of ownership over any recordings. Users are responsible for ensuring their audio files comply with applicable copyright laws.