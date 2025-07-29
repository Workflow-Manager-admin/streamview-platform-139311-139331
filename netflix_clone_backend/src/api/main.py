from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.routers import (
    auth, users, profiles, videos, streaming, subscriptions, payments,
    watch_history, recommendations, parental_controls
)

app = FastAPI(
    title="StreamView Backend (Netflix Clone)",
    description=(
        "Backend REST API for a Netflix clone. Handles authentication, user "
        "management, video catalog/search, streaming, profiles, subscriptions, "
        "payments, watch history, recommendations, multi-profile support, and parental controls."
    ),
    version="1.0.0",
    openapi_tags=[
        {"name": "Auth", "description": "Authentication and Registration"},
        {"name": "Users", "description": "User Management APIs"},
        {"name": "Profiles", "description": "User Profile Management"},
        {"name": "Videos", "description": "Video Catalog, Search and Metadata"},
        {"name": "Streaming", "description": "Video Playback and Streaming APIs"},
        {"name": "Subscriptions", "description": "Subscription Management"},
        {"name": "Payments", "description": "Payments and Billing APIs"},
        {"name": "WatchHistory", "description": "Watch History APIs"},
        {"name": "Recommendations", "description": "Personalized Recommendations"},
        {"name": "ParentalControls", "description": "Parental Controls and Restrictions"}
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health"])
def health_check():
    """Health check endpoint for Netflix Clone backend."""
    return {"message": "Healthy"}

# --- Routers registration for modules ---
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(profiles.router, prefix="/profiles", tags=["Profiles"])
app.include_router(videos.router, prefix="/videos", tags=["Videos"])
app.include_router(streaming.router, prefix="/streaming", tags=["Streaming"])
app.include_router(subscriptions.router, prefix="/subscriptions", tags=["Subscriptions"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(watch_history.router, prefix="/history", tags=["WatchHistory"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])
app.include_router(parental_controls.router, prefix="/parental", tags=["ParentalControls"])
