# Session-Fixation-Checker
The Session-Fixation-Checker is a tool designed to test for session fixation vulnerabilities in web applications. Session fixation is a type of security flaw where an attacker can fixate a session ID before the user logs in, and if the session ID remains unchanged after login, the attacker can hijack the session.

How the Session-Fixation-Checker Works:
  Before Login: User enters the session ID from their browser before logging in.

  After Login: User logs in and enters the new session ID. The tool checks if the session ID changed.

  After Logout: User logs out and enters the session ID again. The tool verifies if the session ID changed.

<img width="841" alt="image" src="https://github.com/user-attachments/assets/df574dd8-ee9f-4369-8407-a63915bea218">

Vulnerability Detection:
If the session ID does not change between these stages (especially between "Before Login" and "After Login"), the tool identifies a session fixation vulnerability.
Importance of Changing Session IDs:
Security: Changing the session ID upon login is crucial for preventing session fixation attacks. If the session ID remains the same, an attacker who knows the session ID before the login can hijack the user's session after they log in.
This tool helps security professionals and developers ensure that their applications are protected against session fixation by confirming that session IDs are properly regenerated upon user authentication.
