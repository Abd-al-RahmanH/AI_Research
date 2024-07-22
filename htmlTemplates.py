css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
}

.chat-message.user {
    background-color: #cccc99; /* rose */
}

.chat-message.bot {
    background-color: #ffcccc; /* green  */
}

.chat-message .avatar {
    width: 20%;
}

.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
    color: #000; /* Black color */
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/7GW6Cws/126174.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/FK6vHLZ/pexels-andrea-piacquadio-774909.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
