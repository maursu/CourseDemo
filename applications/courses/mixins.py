class FormateDateMixin:
    @property
    def created(self):
        return self.created_at.strftime("%Y-%m-%d:%H:%M")

    @property
    def updated(self):
        return self.updated_at.strftime("%Y-%m-%d:%H:%M")
