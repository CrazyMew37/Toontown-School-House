GiveAwardErrors = Enum('Success, WrongGender, NotRewardable, FullMailbox, FullAwardMailbox, AlreadyInMailbox, AlreadyInGiftQueue, '
                       'AlreadyInOrderedQueue, AlreadyInCloset, AlreadyBeingWorn, AlreadyInAwardMailbox, '
                       'AlreadyInThirtyMinuteQueue, AlreadyInMyPhrases, AlreadyKnowDoodleTraining, AlreadyRented, '
                       'GenericAlreadyHaveError, UnknownError, UnknownToon, NonToon, '
                       )

GiveAwardErrorStrings = {
    GiveAwardErrors.Success: "success",
    GiveAwardErrors.WrongGender: "wrong gender",
    GiveAwardErrors.NotRewardable: "item is not rewardable",
    GiveAwardErrors.FullMailbox: "mailbox is full",
    GiveAwardErrors.FullAwardMailbox: "award mailbox is full",
    GiveAwardErrors.AlreadyInMailbox: "award already in mailbox.",
    GiveAwardErrors.AlreadyInGiftQueue: "award already in gift queue.",
    GiveAwardErrors.AlreadyInOrderedQueue: "award already in ordered queue.",
    GiveAwardErrors.AlreadyInCloset: "award already in closet.",
    GiveAwardErrors.AlreadyBeingWorn: "award already being worn.",
    GiveAwardErrors.AlreadyInAwardMailbox: "award already in award mailbox",
    GiveAwardErrors.AlreadyInThirtyMinuteQueue: "award already in 30 minute queue",
    GiveAwardErrors.AlreadyInMyPhrases: "speed chat award already in my phrases",
    GiveAwardErrors.AlreadyKnowDoodleTraining: "doodle training award already known",
    GiveAwardErrors.AlreadyRented: "award is already rented",
    GiveAwardErrors.GenericAlreadyHaveError: "generic-already-have error",
    GiveAwardErrors.UnknownError: "unknown error",
    GiveAwardErrors.UnknownToon: "toon not in database",
    GiveAwardErrors.NonToon: "this is not a toon",
}

assert len(GiveAwardErrorStrings) == len(GiveAwardErrors)
