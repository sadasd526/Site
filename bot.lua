local module = loadstring(game:HttpGet("https://raw.githubusercontent.com/sadasd526/AdoptMeTradeFrameWork/main/main.lua"))()


local websocket = loadstring(game:HttpGet("https://raw.githubusercontent.com/Blue-v3rm/symmetrical-guide/main/client/websocket.lua"))()
local ws = websocket.new("ws://localhost:6789")
ws:init(game:GetService('Players').LocalPlayer.UserId) -- sends your ID as an identifier

coroutine.wrap(function()
	while true do
		game.Players.LocalPlayer.Character.Humanoid:MoveTo(Vector3.new(-10009.3, 3995.7, -4033.37))
		game.Players.LocalPlayer.Character.Humanoid.MoveToFinished:Wait()
		game.Players.LocalPlayer.Character.Humanoid:MoveTo(Vector3.new(-9995.51, 3995.7, -4021.16))
		game.Players.LocalPlayer.Character.Humanoid.MoveToFinished:Wait()
		game.Players.LocalPlayer.Character.Humanoid:MoveTo(Vector3.new(-9988.95, 3995.7, -4028.36))
		game.Players.LocalPlayer.Character.Humanoid.MoveToFinished:Wait()
		game.Players.LocalPlayer.Character.Humanoid:MoveTo(Vector3.new(-9997.53, 3995.7, -4042.03))
		game.Players.LocalPlayer.Character.Humanoid.MoveToFinished:Wait()
	end
end)()

local l__load__1 = require(game.ReplicatedStorage:WaitForChild("Fsys")).load;
local u7 = l__load__1("RouterClient")
local Cooldown = {}
local tab = {}
local BlackList = {}
local TimeCooldown = 5 * 60

function Format(Int)
	return string.format("%02i", Int)
end

function convertToHMS(Seconds)
	local Minutes = (Seconds - Seconds%60)/60
	Seconds = Seconds - Minutes*60
	local Hours = (Minutes - Minutes%60)/60
	Minutes = Minutes - Hours*60
	return Format(Hours).."h"..Format(Minutes).."m"..Format(Seconds).."s"
end

local function Trade(plr, free, Pets)
	
	local args = {
		[1] = "/w "..plr.Name.." Hello: ".. plr.Name,
		[2] = "All"
	}
	


	if free then
		for i, v in Pets do
			module.AddItemToOffer(v)
		end

		module.WaitForAccept()
		module.AcceptTrade()
		module.WaitForConfirm()
		module.ConfirmTrade()
	else
		
		module.WaitForAccept()
		module.AcceptTrade()
		module.WaitForConfirm()
		module.ConfirmTrade()


	end

	
	--TradeAPI/DeclineTrade
	
	-- local data = require(game.ReplicatedStorage.ClientModules.Core.ClientData).get_data()
	-- u7.get("TradeAPI/SendTradeRequest"):FireServer(plr)

	-- while wait() do
	-- 	data = require(game.ReplicatedStorage.ClientModules.Core.ClientData).get_data()
	-- 	print(data[game.Players.LocalPlayer.Name]['trade'])
	-- 	if data[game.Players.LocalPlayer.Name]['trade'] then
	-- 		break
	-- 	end
		
	-- 	wait(1)
	-- end
	
	-- print('trade started')


	-- game:GetService("ReplicatedStorage").DefaultChatSystemChatEvents.SayMessageRequest:FireServer(unpack(args))


	-- -- game:GetService("ReplicatedStorage").API:FindFirstChild("SrbfhEUOGKxxquD/iGrvx"):FireServer()
	-- --local count = 0
	-- --for i, v in pairs(data[game.Players.LocalPlayer.Name]["inventory"]['pets']) do
	-- --	print(i)
	-- --	count = count + 1
	-- --	if count <= 1 then
	-- --		u7.get("TradeAPI/AddItemToOffer"):FireServer(v.unique)
	-- --	end
	-- --end

	-- --wait(5)
	
	-- if free then
	-- 	 --game:GetService("ReplicatedStorage").API:FindFirstChild("SrbfhEUOGKxxquD/iGrvx"):FireServer()
	-- 	local count = 0
	-- 	for i, v in pairs(data[game.Players.LocalPlayer.Name]["inventory"]['pets']) do
	-- 		print(i)
	-- 		count = count + 1
	-- 		if count <= 1 then
	-- 			u7.get("TradeAPI/AddItemToOffer"):FireServer(v.unique)
	-- 		end
	-- 	end
	-- end
	
	-- local data = require(game.ReplicatedStorage.ClientModules.Core.ClientData).get_data()
	
	-- print(data[game.Players.LocalPlayer.Name]['trade']['recipient_offer']['negotiated'])
	
	-- repeat wait(1)
	-- 	data = require(game.ReplicatedStorage.ClientModules.Core.ClientData).get_data()
	-- 	print(BlackList[plr.Name] + 5, tick(), BlackList[plr.Name] + 5 > tick())
	-- 	if BlackList[plr.Name] + 60 < tick() then
	-- 		u7.get("TradeAPI/DeclineTrade"):FireServer()
	-- 		return
	-- 	end
	-- until data[game.Players.LocalPlayer.Name]['trade']['recipient_offer']['negotiated'] == true
	
	-- print('trade AcceptNegotiation')
	-- u7.get("TradeAPI/AcceptNegotiation"):FireServer()
	-- BlackList[plr.Name] = tick()

	-- while wait() do
	-- 	data = require(game.ReplicatedStorage.ClientModules.Core.ClientData).get_data()
	-- 	print(data[game.Players.LocalPlayer.Name]['trade']['recipient_offer']['confirmed'])
	-- 	print(data[game.Players.LocalPlayer.Name]['trade']['sender_offer']['confirmed'])
	-- 	print(BlackList[plr.Name] + 5, tick(), BlackList[plr.Name] + 5 > tick())
	-- 	if BlackList[plr.Name] + 30 < tick() then
	-- 		u7.get("TradeAPI/DeclineTrade"):FireServer()
	-- 		return
	-- 	end
	-- 	if data[game.Players.LocalPlayer.Name]['trade']['recipient_offer']['confirmed'] == true or data[game.Players.LocalPlayer.Name]['trade']['sender_offer']['confirmed'] == true then
	-- 		break
	-- 	end
		

	-- 	wait(1)
	-- end


	-- print('trade ConfirmTrade')
	-- u7.get("TradeAPI/ConfirmTrade"):FireServer()
	-- wait(5)
	-- tab[plr.Name] = true
end

--for _, plr in pairs(game.Players:GetChildren()) do
--	if not tab[plr.Name] and plr.Name ~= game.Players.LocalPlayer.Name then
--		Trade(plr)
--	end
--end

--game.Players.PlayerAdded:Connect(function(plr)
--	Trade(plr)
--end)





--game.Players.LocalPlayer.Chatted:Connect(function(...)
--	print(...)
--end)

--for i, v in pairs(game.Players:GetChildren()) do
--	v.Chatted:Connect(function(...)
--		print(...)
--	end)
--end


--for i, v in pairs(game.Players:GetChildren()) do
--	if not Cooldown[v.Name] then
--		Cooldown[v.Name] = 0
--	end
	
--	v.Chatted:Connect(function(message:string, ...)
--		print(message:lower(), message:lower() == 'deposit')
--		if message:lower() == 'deposit' then
--			u7.get("TradeAPI/SendTradeRequest"):FireServer(v)
--		elseif message:lower() == 'freepet' then
--			u7.get("TradeAPI/SendTradeRequest"):FireServer(v)
--		end
--	end)
--end


-- local chatEvents = game:GetService("ReplicatedStorage"):WaitForChild("DefaultChatSystemChatEvents")
-- local messageDoneFiltering = chatEvents:WaitForChild("OnMessageDoneFiltering")

-- messageDoneFiltering.OnClientEvent:Connect(function(message)
-- 	local player = game.Players:FindFirstChild(message.FromSpeaker)
-- 	local message = message.Message or ""

-- 	if player then
-- 		if message:lower() == 'deposit' then
-- 			Trade(player)
-- 			--u7.get("TradeAPI/SendTradeRequest"):FireServer(player)
-- 		elseif message:lower() == 'freepet' then
			
-- 			if not tab[player.Name] then
-- 				Trade(player, true)
-- 			end
-- 			--u7.get("TradeAPI/SendTradeRequest"):FireServer(player)
-- 		end
-- 	end
-- end)

local PlayerList = {}

-- connec to web socket server and send data
local connection = syn.websocket.connect("ws://localhost:6789/")
ws:init(game:GetService('Players').LocalPlayer.UserId) -- sends your ID as an identifier
connection.OnMessage:Connect(function(call) 
	print(call)
end)
ws:register("OrderPlayer","Player deposits.",function(er)
	print(er)
    -- local PlayerId, IsDepositing, SiteId, Pets  = game:GetService("HttpService"):JsonDecode(er)

	-- -- local Player = game:GetService('Players'):GetPlayerByUserId(PlayerId)
	-- PlayerList[PlayerId] = game:GetService("HttpService"):JsonDecode(er)
    -- -- game:GetService("ReplicatedStorage").DefaultChatSystemChatEvents.SayMessageRequest:FireServer(table.concat(args,"/"),"All")
end)

u7.get_event("TradeAPI/TradeRequestReceived").OnClientEvent:connect(function(p72)
	if PlayerList[p72.UserId] ~= nil then
		u7.get("TradeAPI/AcceptOrDeclineTradeRequest"):InvokeServer(p72, true);
	
		spawn(function()
			Trade(p72)
		end)
	else
		u7.get("TradeAPI/AcceptOrDeclineTradeRequest"):InvokeServer(p72, false);

	end
end);

getgenv().ws = ws


