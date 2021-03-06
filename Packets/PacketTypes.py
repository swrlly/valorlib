class PacketTypes:
    # print("\n".join([re.search("\.toMessage\(.+?\)", x).group()[11:-1] + " = " + re.search("\.map\(.+?\)", x).group()[5:-1]  for x in tmp.split("\n")]))
    Create = 12
    PlayerShoot = 66
    Move = 16
    PlayerText = 47
    UpdateAck = 91
    InvSwap = 25
    UseItem = 1
    Hello = 9
    InvDrop = 18
    Pong = 64
    Load = 26
    SetCondition = 60
    Teleport = 45
    UsePortal = 6
    Buy = 93
    PlayerHit = 10
    EnemyHit = 19
    AoeAck = 77
    ShootAck = 35
    OtherHit = 57
    SquareHit = 13
    GotoAck = 79
    GroundDamage = 98
    GroundTeleporter = 178
    ChooseName = 23
    CreateGuild = 95
    GuildRemove = 49
    GuildInvite = 41
    RequestTrade = 34
    RequestPartyInvite = 168
    ChangeTrade = 55
    AcceptTrade = 3
    CancelTrade = 39
    CheckCredits = 20
    Escape = 87
    GoToQuestRoom = 155
    JoinGuild = 27
    ChangeGuildRank = 11
    EditAccountList = 62
    EnterArena = 48
    OutgoingMessage = 84
    OutgoingMessage = 51
    QuestRedeem = 37
    KeyInfoRequest = 151
    LaunchRaid = 156
    SorForgeRequest = 159
    ForgeItem = 160
    AlertNotice = 163
    QoLAction = 165
    MarkRequest = 164
    UnboxRequest = 161
    MarketCommand = 99
    RequestGamble = 167
    AcceptPartyInvite = 170
    Failure = 0
    CreateSuccess = 81
    ServerPlayerShoot = 92
    Damage = 97
    Update = 42
    Notification = 33
    GlobalNotification = 24
    NewTick = 68
    ShowEffect = 38
    Goto = 30
    InvResult = 63
    Reconnect = 14
    Ping = 85
    MapInfo = 74
    Pic = 46
    Death = 83
    BuyResult = 50
    Aoe = 89
    AccountList = 44
    QuestObjId = 28
    NameResult = 22
    GuildResult = 82
    AllyShoot = 36
    EnemyShoot = 52
    TradeRequested = 80
    GambleStart = 166
    PartyRequest = 169
    TradeStart = 31
    TradeChanged = 4
    TradeDone = 94
    TradeAccepted = 78
    ClientStat = 75
    File = 56
    InvitedToGuild = 58
    PlaySound = 59
    ImminentArenaWave = 5
    ArenaDeath = 17
    VerifyEmail = 61
    ReskinUnlock = 40
    PasswordPrompt = 69
    QuestFetchResponse = 65
    QuestRedeemResponse = 88
    KeyInfoResponse = 152
    SetFocus = 108
    QueuePong = 112
    ServerFull = 110
    QueuePing = 111
    SwitchMusic = 106
    SorForge = 158
    UnboxResultPacket = 162
    MarketResult = 100
    LootNotification = 171
    ShowTrials = 172
    TrialsRequest = 173
    PotionStorageInteraction = 174
    RenameItem = 175
    HomeDepotInteraction = 176
    HomeDepotResult = 177
    ClaimBattlePassItem = 179
    MissionsReceive = 180
    RespriteItem = 181
    Text = 96

    reverseDict = {x[1]: x[0] for x in locals().items() if isinstance(x[1], int)}