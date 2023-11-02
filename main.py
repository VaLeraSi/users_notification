from bson import ObjectId
from fastapi import FastAPI, HTTPException, Query, BackgroundTasks
from config.settings import settings, db
from pydantic_models import NotificationRequest, NotificationKey, ListResponse
from use_cases import sender, create_notification

app = FastAPI()


@app.post("/create", status_code=201)
async def make_notification(
    notification: NotificationRequest, background_tasks: BackgroundTasks
):
    user_id = notification.user_id
    key = notification.key
    target_id = notification.target_id
    data = notification.data

    if key == NotificationKey.registration:
        subject = "Welcome"
        message = "Thank you!"
        background_tasks.add_task(sender.send_email, subject, message)

    elif key in {NotificationKey.new_message, NotificationKey.new_post}:
        await create_notification.create_note(user_id, key, target_id, data)

    elif key == NotificationKey.new_login:
        subject = "Welcome"
        message = "Thank you!"
        background_tasks.add_task(sender.send_email, subject, message)
        await create_notification.create_note(user_id, key, target_id, data)
    return {"success": True}


@app.get("/list", response_model=ListResponse)
async def list_notifications(
    user_id: str = Query(),
    skip: int = Query(0),
    limit: int = Query(10),
):
    user_notifications = (
        await db.notifications.find({"user_id": user_id})
        .skip(skip)
        .to_list(length=limit)
    )
    new_notifications = sum(
        1 for notification in user_notifications if notification.get("is_new")
    )

    response = {
        "success": True,
        "data": {
            "elements": len(user_notifications),
            "new": new_notifications,
            "request": {
                "user_id": user_id,
                "skip": skip,
                "limit": limit,
            },
            "list": user_notifications,
        },
    }

    return response


@app.post("/read")
async def read_mark(
    user_id: str = Query(),
    notification_id: str = Query(),
):
    user_id = user_id
    notification_id = notification_id

    notification = await db.notifications.find_one({"_id": ObjectId(notification_id)})

    if not notification:
        raise HTTPException(status_code=404, detail="Уведомление не найдено")

    if notification["user_id"] != user_id:
        raise HTTPException(
            status_code=403, detail="Уведомление не принадлежит данному пользователю"
        )

    await db.notifications.update_one(
        {"_id": ObjectId(notification_id)}, {"$set": {"is_new": False}}
    )

    return {"success": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.SITE.host, port=settings.SITE.port)
