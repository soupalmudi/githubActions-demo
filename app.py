diff --git a/api/user.js b/api/user.js
index 1111111..2222222 100644
--- a/api/user.js
+++ b/api/user.js
@@
 export async function getUser(req, res) {
-  const user = await db.findById(req.params.id);
-  if (user) res.json(user);
-  res.status(404).json({ error: "Not found" });
+  const user = await db.findById(req.params.id);
+  if (!user) {
+    return res.status(404).json({ error: "Not found" });
+  }
+  res.json(user);
 }
