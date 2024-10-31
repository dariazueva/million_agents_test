class EmailMasker:
    def __init__(self, mask_char="x"):
        self.mask_char = mask_char

    def mask(self, email):
        local, domain = email.split("@")
        return f"{self.mask_char * len(local)}@{domain}"


class PhoneMasker:
    def __init__(self, mask_char="x", mask_length=3):
        self.mask_char = mask_char
        self.mask_length = mask_length

    def mask(self, phone_number):
        parts = phone_number.split()
        flattened_number = "".join(parts)
        visible_length = len(flattened_number) - self.mask_length
        masked_number = (
            flattened_number[:visible_length] + self.mask_char * self.mask_length
        )
        masked_parts = []
        index = 0
        for part in parts:
            masked_parts.append(masked_number[index : index + len(part)])
            index += len(part)
        return " ".join(masked_parts)


class SkypeMasker:
    def __init__(self, mask_char="x"):
        self.mask_char = mask_char

    def mask(self, skype_id):
        if skype_id.startswith("skype:"):
            masked_id = "skype:" + self.mask_char * 3
            return (
                masked_id
                if "?" not in skype_id
                else skype_id.replace("skype:", masked_id, 1)
            )
        return skype_id


print(EmailMasker().mask("example@domain.com"))  # "xxxxxxx@domain.com"

print(PhoneMasker(mask_length=5).mask("+7 666 777 888"))  # "+7 666 7xx xxx"

print(SkypeMasker().mask("skype:alex.max"))  # "skype:xxx"
print(
    SkypeMasker().mask('<a href="skype:alex.max?call">skype</a>')
)  # '<a href="skype:xxx?call">skype</a>'
