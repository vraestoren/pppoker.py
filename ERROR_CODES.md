## PPPoker Response Codes

Extracted from IL2CPP `dump.cs`.

### `AddActionTimeErrCode`

| Code | Name |
|---:|---|
| `-3` | `AddActionTimeErrOverMaxTimes` |
| `-2` | `AddActionTimeErrNotInSeat` |
| `-1` | `AddActionTimeErrNotEnoughDiamond` |
| `0` | `AddActionTimeOk` |

### `AddUnlimitedPPChipsErrorCode`

| Code | Name |
|---:|---|
| `-5` | `AddUnlimitedChipsNoClubQuota` |
| `-4` | `AddUnlimitedChipsNoQuota` |
| `-3` | `AddUnlimitedChipsInvalid` |
| `-2` | `AddUnlimitedChipsNoAuth` |
| `-1` | `AddUnlimitedChipsNoMoney` |
| `0` | `AddUnlimitedChipsOk` |

### `AssetDeliveryErrorCode`

| Code | Name |
|---:|---|
| `0` | `NoError` |
| `1` | `AppUnavailable` |
| `2` | `BundleUnavailable` |
| `3` | `NetworkError` |
| `4` | `AccessDenied` |
| `7` | `InsufficientStorage` |
| `8` | `AssetBundleLoadingError` |
| `9` | `Canceled` |
| `10` | `InternalError` |
| `11` | `PlayStoreNotFound` |
| `12` | `NetworkUnrestricted` |
| `13` | `AppNotOwned` |
| `14` | `ConfirmationNotRequired` |
| `15` | `UnrecognizedInstallation` |

### `AuthorizationErrorCode`

| Code | Name |
|---:|---|
| `1000` | `Unknown` |
| `1001` | `Canceled` |
| `1002` | `InvalidResponse` |
| `1003` | `NotHandled` |
| `1004` | `Failed` |

### `BingoRewardClaimCode`

| Code | Name |
|---:|---|
| `-3` | `AlreadyClaimed` |
| `-2` | `DbError` |
| `-1` | `Failed` |
| `0` | `Ok` |

### `BlindLimitCode`

| Code | Name |
|---:|---|
| `-5` | `LimitFailNotMember` |
| `-4` | `LimitFailPermissionDenied` |
| `-3` | `LimitFailNotAgent` |
| `-2` | `LimitFailNotManager` |
| `-1` | `LimitFailParamError` |
| `0` | `LimitSuccess` |

### `BookSeatCode`

| Code | Name |
|---:|---|
| `-13` | `BookErrBanPlay` |
| `-12` | `BookErrRoomFull` |
| `-11` | `BookErrRoomOver` |
| `-10` | `BookErrGpsInvalid` |
| `-9` | `BookErrIp` |
| `-8` | `BookErrGps` |
| `-7` | `BookErrClub` |
| `-6` | `BookErrBeenBooked` |
| `-5` | `BookErrBeenSited` |
| `-4` | `BookErrAlreadySit` |
| `-3` | `BookErrAlreadyBooked` |
| `-2` | `BookErrSeatid` |
| `-1` | `BookErrWaitAuth` |
| `0` | `BookOk` |
| `1` | `BookCancelOk` |

### `CallGameRetCode`

| Code | Name |
|---:|---|
| `-1` | `Error` |
| `0` | `Suuccess` |
| `1` | `HadCallgame` |
| `2` | `GoldNoEnough` |
| `3` | `LimitTimes` |
| `4` | `LimitConcurrency` |
| `5` | `LimitObserver` |
| `6` | `LimitRoom` |
| `7` | `LimitSitedSize` |

### `CallTimeConfirmCode`

| Code | Name |
|---:|---|
| `0` | `WaitConfirmEnterRoom` |
| `1` | `ConfirmEnterRoom` |

### `ClubAICreateRoomErrorCode`

| Code | Name |
|---:|---|
| `-3` | `DbError` |
| `-2` | `NoModules` |
| `-1` | `Unauthorized` |
| `0` | `None` |

### `ClubBagpackOperateCode`

| Code | Name |
|---:|---|
| `0` | `BagpackSuccess` |
| `1` | `BagpackAwardprizesFailure` |
| `2` | `BagpackRegisterFailure` |
| `3` | `BagpackQueryTicketFailure` |
| `4` | `BagpackNoHandle` |
| `5` | `BagpackListFailure` |
| `6` | `BagpackNoTicket` |
| `7` | `BagpackUseTicketFailure` |
| `8` | `BagpackInsertFlowFailure` |
| `9` | `BagpackCancelTicketFailure` |
| `10` | `BagpackDelFailure` |
| `11` | `BagpackTicketExpired` |

### `ClubGetAgentDataV2RSPCode`

| Code | Name |
|---:|---|
| `-2` | `ERROR_NO_AUTHORITY` |
| `-1` | `ERROR_PARAM_ERROR` |
| `0` | `SUCCESS` |

### `ClubSetAgentPPCoinRSPCode`

| Code | Name |
|---:|---|
| `-5` | `ERROR_CHIP_SEND_LIMIT` |
| `-4` | `ERROR_OVER_MAX_PPCOIN` |
| `-2` | `ERROR_MANAGER_NO_AUTHORITY` |
| `-1` | `ERROR_SEND_CHIP_INSUFFICIENT` |
| `0` | `SUCCESS` |

### `ClubSetAgentUserRSPCode`

| Code | Name |
|---:|---|
| `-2` | `ERROR_MANAGER_NO_AUTHORITY` |
| `0` | `SUCCESS` |

### `ClubSetRoleRSPCode`

| Code | Name |
|---:|---|
| `-6` | `ERROR_MANAGER_NO_AUTHORITY` |
| `-3` | `ERROR_CANNOT_SET_ADMIN` |
| `-1` | `ERROR_CLUB_STAR_NEED_LEVEL_UP` |
| `0` | `SUCCESS` |

### `ClubSuspendAgentRSPCode`

| Code | Name |
|---:|---|
| `-5` | `ERROR_CLUB_AGENT_FAILED_5` |
| `-4` | `ERROR_CLUB_AGENT_FAILED_4` |
| `-3` | `ERROR_CLUB_AGENT_FAILED_3` |
| `-2` | `ERROR_CLUB_AGENT_FAILED_2` |
| `-1` | `ERROR_CLUB_AGENT_FAILED_1` |
| `0` | `SUCCESS` |

### `CrashWithdrawRSPCode`

| Code | Name |
|---:|---|
| `-3` | `AlreadyWithdraw` |
| `-2` | `NoBetInfo` |
| `-1` | `WithdrawFailed` |
| `0` | `Success` |

### `CreateClubRoomErrorCode`

| Code | Name |
|---:|---|
| `-1000` | `CreateClubRoomEcClientVersionTooLow` |
| `-201` | `CreateClubRoomEcPpsrBlindLevelInvalid` |
| `-200` | `CreateClubRoomEcPpsrPermissionError` |
| `-22` | `CreateClubRoomEcCreateRoomMaxLimit` |
| `-21` | `CreateClubRoomEcCreationDisabled` |
| `-20` | `CreateClubRoomEcRussianPokerDisabled` |
| `-15` | `CreateClubRoomEcBanClub` |
| `-13` | `CreateClubRoomEcBanLeague` |
| `-12` | `CreateClubRoomEcGetBanned` |
| `-11` | `CreateClubRoomEcJackpotRoomCreationError` |
| `-10` | `CreateClubRoomEcJackpotNotActivated` |
| `-9` | `CreateClubRoomEcRoomNotOpen` |
| `-8` | `CreateClubRoomEcNotInWhiteList` |
| `-7` | `CreateClubRoomEcCannotCreateMicroRoom` |
| `-6` | `CreateClubRoomEcNoPermission` |
| `-5` | `CreateClubRoomEcDiamondNotEnough` |
| `-4` | `CreateClubRoomEcClubExpired` |
| `-3` | `CreateClubRoomEcStopServer` |
| `-2` | `CreateClubRoomEcServerError` |
| `-1` | `CreateClubRoomEcParamError` |
| `0` | `CreateClubRoomEcSuccess` |

### `DisbandLeagueCode`

| Code | Name |
|---:|---|
| `-6` | `DisbandErrIsFixedCost` |
| `-5` | `DisbandErrInPpsx` |
| `-4` | `DisbandErrHasEvent` |
| `-3` | `DisbandErrHasTable` |
| `-2` | `DisbandErrNotCreator` |
| `-1` | `DisbandErrNotExist` |
| `0` | `DisbandSucceed` |

### `ErrorCodes`

| Code | Name |
|---:|---|
| `-16` | `FailedToAllocatePayloadBecauseOfItsSize` |
| `-15` | `FailedToParseMessage` |
| `-14` | `FailedToCreateDisjointedBuffer` |
| `-13` | `UnknownTypeId` |
| `-12` | `UnableToRetrieveContextDataFromLogMessageBuffer` |
| `-11` | `UnableToRetrieveValidContextArgumentIndex` |
| `-10` | `UnableToRetrieveContextArgument` |
| `-9` | `UnableToRetrieveMessageFromContextBuffer` |
| `-8` | `UnableToRetrieveValidPayloadsFromDisjointedMessageBuffer` |
| `-7` | `UnableToRetrieveDisjointedMessageBuffer` |
| `-6` | `UnableToRetrieveSimpleMessageBuffer` |
| `-5` | `UnableToRetrieveDecoratorsInfo` |
| `-4` | `UnableToRetrieveStackTrace` |
| `-3` | `UnableToRetrieveTimestampAndLevel` |
| `-2` | `FailedToLockPayloadBuffer` |
| `-1` | `CorruptedDecorationInfo` |
| `0` | `NoError` |

### `FtpStatusCode`

| Code | Name |
|---:|---|
| `0` | `Undefined` |
| `110` | `RestartMarker` |
| `120` | `ServiceTemporarilyNotAvailable` |
| `125` | `DataAlreadyOpen` |
| `150` | `OpeningData` |
| `200` | `CommandOK` |
| `202` | `CommandExtraneous` |
| `212` | `DirectoryStatus` |
| `213` | `FileStatus` |
| `215` | `SystemType` |
| `220` | `SendUserCommand` |
| `221` | `ClosingControl` |
| `226` | `ClosingData` |
| `227` | `EnteringPassive` |
| `230` | `LoggedInProceed` |
| `234` | `ServerWantsSecureSession` |
| `250` | `FileActionOK` |
| `257` | `PathnameCreated` |
| `331` | `SendPasswordCommand` |
| `332` | `NeedLoginAccount` |
| `350` | `FileCommandPending` |
| `421` | `ServiceNotAvailable` |
| `425` | `CantOpenData` |
| `426` | `ConnectionClosed` |
| `450` | `ActionNotTakenFileUnavailableOrBusy` |
| `451` | `ActionAbortedLocalProcessingError` |
| `452` | `ActionNotTakenInsufficientSpace` |
| `500` | `CommandSyntaxError` |
| `501` | `ArgumentSyntaxError` |
| `502` | `CommandNotImplemented` |
| `503` | `BadCommandSequence` |
| `530` | `NotLoggedIn` |
| `532` | `AccountNeeded` |
| `550` | `ActionNotTakenFileUnavailable` |
| `551` | `ActionAbortedUnknownPageType` |
| `552` | `FileActionAborted` |
| `553` | `ActionNotTakenFilenameNotAllowed` |

### `GetCheckCode`

| Code | Name |
|---:|---|
| `-9999` | `NULL_RESULT` |
| `0` | `SUCCESS` |
| `268439554` | `ERROR_EMAIL_UNVERIFIED` |
| `268439557` | `ERROR_EMAIL_UNVERIFIED_2` |
| `268443649` | `ERROR_EMAIL_CODE_EXPIRED` |
| `268443650` | `ERROR_VERIFICATION_CODE_ERROR` |
| `268443652` | `ERROR_VERIFICATION_CODE_ERROR2` |

### `GetVerificationCodeResultCode`

| Code | Name |
|---:|---|
| `-9999` | `NULL_RESULT` |
| `0` | `SUCCESS` |
| `268439554` | `ERROR_MAIL_UNVERIFIED` |
| `268439557` | `ERROR_MAIL_UNVERIFIED_2` |
| `268443649` | `ERROR_MAIL_CODE_EXPIRED` |

### `GoogleBillingPurchaseResultCode`

| Code | Name |
|---:|---|
| `0` | `Success` |
| `1` | `Canceled` |
| `2` | `Failed` |

### `GuessHandRETCode`

| Code | Name |
|---:|---|
| `-1` | `Error` |
| `0` | `Suuccess` |
| `1` | `HadGuess` |
| `2` | `GoldNoEnough` |
| `3` | `WatcherCannotGuess` |
| `4` | `NotGetrandopt` |
| `5` | `WatcherCannotGetrandopt` |
| `6` | `GameModeWrong` |
| `7` | `RoomTypeWrong` |
| `8` | `RoomModeWrong` |

### `HeadFrameGrantCode`

| Code | Name |
|---:|---|
| `0` | `HeadframeGrantSuccess` |
| `1` | `HeadframeGrantFailed` |
| `2` | `HeadframeGrantAlreadyGranted` |
| `3` | `HeadframeGrantNotInActivityTime` |

### `HttpStatusCode`

| Code | Name |
|---:|---|
| `100` | `Continue` |
| `101` | `SwitchingProtocols` |
| `102` | `Processing` |
| `103` | `EarlyHints` |
| `200` | `OK` |
| `201` | `Created` |
| `202` | `Accepted` |
| `203` | `NonAuthoritativeInformation` |
| `204` | `NoContent` |
| `205` | `ResetContent` |
| `206` | `PartialContent` |
| `207` | `MultiStatus` |
| `208` | `AlreadyReported` |
| `226` | `IMUsed` |
| `300` | `MultipleChoices` |
| `300` | `Ambiguous` |
| `301` | `MovedPermanently` |
| `301` | `Moved` |
| `302` | `Found` |
| `302` | `Redirect` |
| `303` | `SeeOther` |
| `303` | `RedirectMethod` |
| `304` | `NotModified` |
| `305` | `UseProxy` |
| `306` | `Unused` |
| `307` | `TemporaryRedirect` |
| `307` | `RedirectKeepVerb` |
| `308` | `PermanentRedirect` |
| `400` | `BadRequest` |
| `401` | `Unauthorized` |
| `402` | `PaymentRequired` |
| `403` | `Forbidden` |
| `404` | `NotFound` |
| `405` | `MethodNotAllowed` |
| `406` | `NotAcceptable` |
| `407` | `ProxyAuthenticationRequired` |
| `408` | `RequestTimeout` |
| `409` | `Conflict` |
| `410` | `Gone` |
| `411` | `LengthRequired` |
| `412` | `PreconditionFailed` |
| `413` | `RequestEntityTooLarge` |
| `414` | `RequestUriTooLong` |
| `415` | `UnsupportedMediaType` |
| `416` | `RequestedRangeNotSatisfiable` |
| `417` | `ExpectationFailed` |
| `421` | `MisdirectedRequest` |
| `422` | `UnprocessableEntity` |
| `423` | `Locked` |
| `424` | `FailedDependency` |
| `426` | `UpgradeRequired` |
| `428` | `PreconditionRequired` |
| `429` | `TooManyRequests` |
| `431` | `RequestHeaderFieldsTooLarge` |
| `451` | `UnavailableForLegalReasons` |
| `500` | `InternalServerError` |
| `501` | `NotImplemented` |
| `502` | `BadGateway` |
| `503` | `ServiceUnavailable` |
| `504` | `GatewayTimeout` |
| `505` | `HttpVersionNotSupported` |
| `506` | `VariantAlsoNegotiates` |
| `507` | `InsufficientStorage` |
| `508` | `LoopDetected` |
| `510` | `NotExtended` |
| `511` | `NetworkAuthenticationRequired` |

### `JoinWaitingListCode`

| Code | Name |
|---:|---|
| `-24` | `JoinErrGpsInvalid` |
| `-23` | `JoinErrIpLimit` |
| `-22` | `JoinErrGpsLimit` |
| `-21` | `JoinErrBanPlay` |
| `-20` | `JoinErrEmailLimit` |
| `-19` | `JoinErrPcLimit` |
| `-18` | `JoinErrVpipPerSet` |
| `-16` | `JoinErrHandsNum` |
| `-15` | `JoinErrVpip` |
| `-7` | `JoinErrWaitAuth` |
| `-6` | `JoinErrClubExpired` |
| `-5` | `JoinErrCannotGetBalance` |
| `-4` | `JoinErrTableIsNotFull` |
| `-3` | `JoinErrTableCannotWait` |
| `-2` | `JoinErrAlreadyWaited` |
| `-1` | `JoinErrAlreadySited` |
| `0` | `JoinSucceed` |

### `KickClubUserRSPCode`

| Code | Name |
|---:|---|
| `-5` | `ERROR_USER_IN_RING` |
| `-4` | `ERROR_USER_IN_MTT` |
| `-3` | `ERROR_MANAGER_NO_AUTHORITY` |
| `-2` | `ERROR_USER_NO_AUTHORITY` |
| `-1` | `ERROR_USER_IS_NOT_CLUB_MEMBER` |
| `0` | `SUCCESS` |

### `KickRoomUserCode`

| Code | Name |
|---:|---|
| `-6` | `NoPermission` |
| `-5` | `TimeLimitTable` |
| `-4` | `NoUser` |
| `-3` | `KickManager` |
| `-2` | `DoingRisk` |
| `-1` | `NoTable` |
| `0` | `Success` |

### `LoadImageErrorCode`

| Code | Name |
|---:|---|
| `0` | `OK` |
| `1` | `BAD_IMAGE` |
| `2` | `NOT_IMPLEMENT` |
| `3` | `AOT_ASSEMBLY_NOT_FIND` |
| `4` | `HOMOLOGOUS_ONLY_SUPPORT_AOT_ASSEMBLY` |
| `5` | `HOMOLOGOUS_ASSEMBLY_HAS_LOADED` |
| `6` | `INVALID_HOMOLOGOUS_MODE` |
| `7` | `PDB_BAD_FILE` |
| `8` | `UNKNOWN_IMAGE_FORMAT` |
| `9` | `UNSUPPORT_FORMAT_VERSION` |
| `10` | `UNSUPPORT_ENCRYPTION_ALGORHITHM` |
| `11` | `DHE_NOT_DIFFERENTIAL_HYBRID_ASSEMBLY` |
| `12` | `DHE_HAS_BEEN_LOADED` |
| `13` | `DHE_BAD_DHAO_DATA` |
| `14` | `DHE_BAD_META_VERSION_FILE` |

### `LoginResultCode`

| Code | Name |
|---:|---|
| `-9999` | `NULL_RESULT` |
| `-100` | `ERROR_SERVER_SERVICE_LIMIT` |
| `-18` | `ERROR_KOR_USER_KYC_EXPIRED` |
| `-17` | `ERROR_KOR_USER_KYC` |
| `-16` | `ERROR_CLUB_FIXEDCOST_LOGINTIP` |
| `-15` | `ERROR_NEED_VERIFY_MAIL` |
| `-14` | `ERROR_PC_LOGINING` |
| `-13` | `ERROR_LOGIN_FORBID` |
| `-12` | `ERROR_REGISTER_MUCH` |
| `-11` | `ERROR_REGIN_UNAVAILABLE` |
| `-10` | `ERROR_GUEST_REGISTER_MUCH` |
| `-9` | `ERROR_ACCOUNT_LOCKED` |
| `-8` | `ERROR_REGISTER_FORBID_2` |
| `-7` | `ERROR_REGISTER_FORBID` |
| `-6` | `ERROR_WELLCOME_TEST` |
| `-5` | `ERROR_SERVER_CLOSED` |
| `-3` | `ERROR_ACCOUNT_OR_PASSWORD_WRONG` |
| `-2` | `ERROR_AUTO_LOGIN_FAILED` |
| `-1` | `ERROR_LOGIN_FAILED` |
| `0` | `SUCCESS` |

### `MarkClubMemberRSPCode`

| Code | Name |
|---:|---|
| `-7` | `ERROR_CANNOT_CERTIFY_OTHER_MANAGERS_AND_THE_HOST` |
| `-6` | `ERROR_NO_PERMISSION` |
| `-5` | `ERROR_NAME_INVALID` |
| `-4` | `ERROR_MARK_FAILED` |
| `-3` | `ERROR_CLUB_MEMBER_NOT_FOUND` |
| `-2` | `ERROR_NOT_THE_CLUB_MANAGER` |
| `-1` | `ERROR_CLUB_NOT_FOUND` |
| `0` | `SUCCESS` |

### `PurchaseGiftBagRetCode`

| Code | Name |
|---:|---|
| `-4` | `GiftbagRetCodePurchased` |
| `-3` | `GiftbagRetCodeFailed` |
| `-2` | `GiftbagRetCodeParamInvalid` |
| `-1` | `GiftbagRetCodeDiamondNotEnough` |
| `0` | `GiftbagRetCodeSucc` |

### `PushMsgErrorCode`

| Code | Name |
|---:|---|
| `-6` | `PushMsgMatchNotJoinable` |
| `-5` | `PushMsgTableNotExist` |
| `-4` | `PushMsgExceedLimit` |
| `-3` | `PushMsgDbError` |
| `-2` | `PushMsgKeyword` |
| `-1` | `PushMsgNoAuth` |
| `0` | `PushMsgOk` |

### `RankListGoldRetCode`

| Code | Name |
|---:|---|
| `-1` | `Fail` |
| `0` | `Success` |

### `RankListRetCode`

| Code | Name |
|---:|---|
| `-1` | `Fail` |
| `0` | `Success` |

### `RegisterEmailAccountResultCode`

| Code | Name |
|---:|---|
| `-9999` | `NULL_RESULT` |
| `-4` | `ERROR_ACCOUNT_HAS_BEEN_BANNED` |
| `-3` | `ERROR_NICKNAME_ALREADY_EXISTS` |
| `-2` | `ERROR_MAX_REGISTRATIONS_REACHED` |
| `-1` | `ERROR_USERNAME_ALREADY_EXISTS` |
| `0` | `SUCCESS` |

### `RussianPokerBetErrorCode`

| Code | Name |
|---:|---|
| `-7` | `RussianPokerBetErrorExceedBonusBetLimit` |
| `-6` | `RussianPokerBetErrorExceedInsuranceLimit` |
| `-5` | `RussianPokerBetErrorLessThanAnte` |
| `-4` | `RussianPokerBetErrorExceedAnteLimit` |
| `-3` | `RussianPokerBetErrorInvalidBetType` |
| `-2` | `RussianPokerBetErrorNotEnoughChips` |
| `-1` | `RussianPokerBetErrorInvalidBet` |
| `0` | `RussianPokerBetErrorNone` |

### `SekaActionRetCode`

| Code | Name |
|---:|---|
| `-2` | `SekaActionErrInvalidChips` |
| `-1` | `SekaActionErrInvalidAction` |
| `0` | `SekaActionOk` |

### `SelfLobbyLimitCode`

| Code | Name |
|---:|---|
| `0` | `SelfLobbyLimitOk` |
| `1` | `SelfLobbyLimitInvalidDays` |
| `2` | `SelfLobbyLimitAlreadySet` |

### `SitDownCode`

| Code | Name |
|---:|---|
| `-101` | `SitErrPlayerSelflimit` |
| `-100` | `SitErrPlayerLosslimit` |
| `-27` | `SitErrDiamond` |
| `-26` | `SitErrBanPlay` |
| `-24` | `SitErrFlashHasNewTable` |
| `-23` | `SitErrValidMail` |
| `-22` | `SitErrPcBan` |
| `-21` | `SitErrLeagueid` |
| `-20` | `SitErrClubid` |
| `-19` | `SitErrPasswd` |
| `-18` | `SitErrVpipPerSet` |
| `-17` | `SitErrAntiCollusion` |
| `-16` | `SitErrHandsNum` |
| `-15` | `SitErrVpip` |
| `-14` | `SitErrBooked` |
| `-13` | `SitErrRoomFull` |
| `-12` | `SitErrRoomOver` |
| `-11` | `SitErrTicket` |
| `-10` | `SitErrGpsInvalid` |
| `-9` | `SitErrIp` |
| `-8` | `SitErrGps` |
| `-7` | `SitErrClub` |
| `-6` | `SitErrWaitlistNotEmpty` |
| `-5` | `SitErrAlreadyStarted` |
| `-4` | `SitErrSeatid` |
| `-3` | `SitErrAlreadySited` |
| `-2` | `SitErrNotEmpty` |
| `-1` | `SitErrMoney` |
| `0` | `SitDownOk` |
| `1` | `SitWaitAuth` |
| `2` | `SitDownOkNewSeat` |

### `SmtpStatusCode`

| Code | Name |
|---:|---|
| `-1` | `GeneralFailure` |
| `211` | `SystemStatus` |
| `214` | `HelpMessage` |
| `220` | `ServiceReady` |
| `221` | `ServiceClosingTransmissionChannel` |
| `250` | `Ok` |
| `251` | `UserNotLocalWillForward` |
| `252` | `CannotVerifyUserWillAttemptDelivery` |
| `354` | `StartMailInput` |
| `421` | `ServiceNotAvailable` |
| `450` | `MailboxBusy` |
| `451` | `LocalErrorInProcessing` |
| `452` | `InsufficientStorage` |
| `454` | `ClientNotPermitted` |
| `500` | `CommandUnrecognized` |
| `501` | `SyntaxError` |
| `502` | `CommandNotImplemented` |
| `503` | `BadCommandSequence` |
| `504` | `CommandParameterNotImplemented` |
| `530` | `MustIssueStartTlsFirst` |
| `550` | `MailboxUnavailable` |
| `551` | `UserNotLocalTryAlternatePath` |
| `552` | `ExceededStorageAllocation` |
| `553` | `MailboxNameNotAllowed` |
| `554` | `TransactionFailed` |

### `StandUpCode`

| Code | Name |
|---:|---|
| `-101` | `PlayerSelflimit` |
| `-100` | `PlayerLosslimit` |
| `-18` | `VpipPerSetInvalid` |
| `-1` | `ErrorStand` |
| `0` | `NormalStand` |
| `1` | `NoChipsStand` |
| `2` | `ClubRoomTimeUpStand` |
| `3` | `NoActionStand` |
| `4` | `SystemStand` |
| `5` | `LadderOverStand` |
| `6` | `ChangeTableStand` |
| `7` | `KickedStand` |
| `8` | `FinalRewardStand` |
| `9` | `LackGpsStand` |
| `10` | `BreakGpsIpRuleStand` |
| `11` | `ZoomFoldStand` |
| `12` | `CalltimeCancel` |
| `13` | `CaptchaStand` |
| `14` | `TimeLimitStand` |
| `15` | `NoSquidChipsStand` |
| `16` | `PlayerLogoutStand` |
| `17` | `AchievedTargetStackStand` |

### `StatusCode`

| Code | Name |
|---:|---|
| `-11` | `NetworkSocketError` |
| `-10` | `NetworkReceiveQueueFull` |
| `-9` | `NetworkArgumentMismatch` |
| `-8` | `NetworkSendHandleInvalid` |
| `-7` | `NetworkDriverParallelForErr` |
| `-6` | `NetworkHeaderInvalid` |
| `-5` | `NetworkSendQueueFull` |
| `-4` | `NetworkPacketOverflow` |
| `-3` | `NetworkStateMismatch` |
| `-2` | `NetworkVersionMismatch` |
| `-1` | `NetworkIdMismatch` |
| `0` | `Success` |

### `TableNoticeCode`

| Code | Name |
|---:|---|
| `-1` | `CannotLeaveTable` |
| `3` | `PpCoinProfitOver100Bb` |
| `4` | `StoreReview` |
| `5` | `FoldAndLeaveAfter31` |
| `6` | `StandUpAfterHand` |
| `7` | `ExitAfterHand` |

### `TenthAnniRewardCode`

| Code | Name |
|---:|---|
| `0` | `TenthAnniRewardSuccess` |
| `1` | `TenthAnniRewardNotInActivityTime` |
| `2` | `TenthAnniRewardMissionNotAchieved` |
| `3` | `TenthAnniRewardAlreadyReward` |

### `VIPRetCode`

| Code | Name |
|---:|---|
| `-4` | `AreadyGet` |
| `-3` | `Failed` |
| `-2` | `ParamInvalid` |
| `-1` | `DiamondNotEnough` |
| `0` | `Succ` |

### `VersionResultCode`

| Code | Name |
|---:|---|
| `-1` | `StopService` |
| `-1` | `StopService` |
| `0` | `OK` |
| `0` | `OK` |
| `1` | `NeedUpdate` |
| `1` | `NeedUpdate` |
| `2` | `ForceUpdate` |
| `2` | `ForceUpdate` |

