from rest_framework import serializers

from send_mess.models import Message, Send


class SendSerializers(serializers.ModelSerializer):
    count_sent_message = serializers.SerializerMethodField(read_only=True,)
    count_unsent_message = serializers.SerializerMethodField(read_only=True,)

    class Meta:
        model = Send
        fields = "__all__"

    def get_count_sent_message(self, obj):
        return len(obj.sends.filter(status=True))

    def get_count_unsent_message(self, obj):
        return len(obj.sends.filter(status=False))


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"
