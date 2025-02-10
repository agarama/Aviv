async function getSecretToken() {
    try {
        const response = await fetch('/get-secret'); // יש להגדיר נתיב מאובטח בשרת
        const data = await response.json();
        return data.token;
    } catch (error) {
        console.error("❌ שגיאה בטעינת הטוקן:", error);
        return null;
    }
}
