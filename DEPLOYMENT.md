# 🚀 Deployment Guide

## Quick Deploy Options

### Option 1: Render (Recommended - Free)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect the `render.yaml` file
   - Click "Create Web Service"
   - Wait for deployment (it will auto-train the model)

3. **Access your API:**
   - Your API will be live at: `https://your-app-name.onrender.com`
   - API docs: `https://your-app-name.onrender.com/docs`

---

### Option 2: Railway

1. **Push to GitHub** (same as above)

2. **Deploy on Railway:**
   - Go to [railway.app](https://railway.app)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway will use the `Procfile`
   - Add build command: `pip install -r requirements.txt && python train.py`
   - Deploy!

---

### Option 3: Fly.io

1. **Install Fly CLI:**
   ```bash
   # Windows (PowerShell)
   iwr https://fly.io/install.ps1 -useb | iex
   ```

2. **Deploy:**
   ```bash
   fly launch
   fly deploy
   ```

---

## Important Notes

### ✅ What Works in Production:
- All API endpoints
- ML model predictions
- SQLite database (for small-scale use)
- Automatic model training on deployment

### ⚠️ Considerations:

1. **Database:** SQLite works fine for demos but for production with high traffic, consider PostgreSQL
2. **Model Training:** The model is trained during deployment (takes ~10 seconds)
3. **Cold Starts:** Free tiers may have cold starts (first request might be slow)
4. **File Storage:** Model files persist on Render/Railway

### 🔧 Environment Variables (Optional):

If you want to configure anything:
- `PORT` - Auto-set by hosting platform
- `DATABASE_URL` - If you want to use PostgreSQL instead of SQLite

---

## Testing Your Deployed API

Once deployed, test with:

```bash
# Health check
curl https://your-app.onrender.com/health

# Predict
curl -X POST "https://your-app.onrender.com/ml/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "I want to book an appointment"}'

# Ingest message
curl -X POST "https://your-app.onrender.com/messages/ingest" \
  -H "Content-Type: application/json" \
  -d '{"from": "+1234567890", "text": "I need my test results"}'
```

---

## Troubleshooting

### Issue: Model not loading
**Solution:** Ensure `python train.py` runs in build command

### Issue: Port binding error
**Solution:** Make sure app uses `--host 0.0.0.0 --port $PORT`

### Issue: Dependencies not installing
**Solution:** Check `requirements.txt` includes all packages

---

## 🎉 Your API is Production-Ready!

The project is designed to work seamlessly on hosting platforms. Just push to GitHub and deploy!
