pragma solidity ^0.5.13;

contract EDToken {
    
    uint prize = 1;
    
    uint supply;
    uint totalRoutes;
    uint totalUsers;
    uint startTime;
    
    struct Route {
        uint id;
        uint[] users;
        string name;
        string startPosition;
        string endPosition;
    }
    struct User {
        uint id;
        string name;
        address wallet_address;
        uint[] routes;
    }
    
    
    struct UnR {
        uint user_id;
        uint route_id;
    }
    
    struct Score {
        uint tries;
        uint fuelConsumption;
    }
    
    struct LeaderboardEntry {
        bool exists;
        uint user_id;
        uint score;
    }
    
    mapping (uint => Route) routes;
    mapping (uint => User) users;

    mapping (address => uint) wallets; //user_id to amount
    mapping (uint => mapping (uint => Score)) unrScore;
    mapping(uint => LeaderboardEntry) winners; //route_id to Score
    mapping(address => mapping (address => uint256)) allowed;
    
    event Transfer(address from, address to, uint amount);
    event Approval(address from, address to, uint amount);
    event ScoreEvent(uint user_id, uint route_id, uint score);
    event WinnerEvent(uint user_id, uint amount);
    event DriveEvent(uint user_id, uint route_id, uint amount);
    event RouteEvent(uint route_id, string name, string startPosition, string endPosition);
    event UserEvent(uint user_id, string name, address wallet_address);
    event SubscribeEvent(uint user_id, uint route_id);
    
    constructor() public {
        supply = 100;
        totalRoutes = 0;
        totalUsers = 0;
        wallets[msg.sender] = supply;
        startTime = block.timestamp;
    }
    
    modifier isAllowed (address a, uint amount) {
        require (allowed[msg.sender][a] >= amount);
        _;
    }
    
    function totalSupply() view public 
    returns (uint s) {
        s = supply;
    }
    
    function balanceOf(address a) view public
    returns (uint balance) {
        balance = wallets[a];
    }
    
    function transfer(address reciever, uint amount) public {
        wallets[reciever] += amount;
        wallets[msg.sender] -= amount;
        emit Transfer(msg.sender, reciever, amount);
    }
    
    function transferFrom(address sender, address reciever, uint amount) public isAllowed(sender, amount) {
        wallets[reciever] += amount;
        wallets[msg.sender] -= amount;
        allowed[msg.sender][sender] -= amount;
        emit Transfer(sender, reciever, amount);
    }
    
    function approve(address delegate, uint a) public {
        allowed[msg.sender][delegate] = a;
        emit Approval(msg.sender, delegate, a);
    }
    
    function allowance(address owner, address delegate) view public
    returns (uint amount) {
        amount = allowed[owner][delegate];
    }
    
    function addDrive(uint user_id, uint route_id, uint fuelConsumed) public {
        if (block.timestamp >= startTime + 2 minutes) {
            totalRecall();
            startTime = block.timestamp;
        }
        unrScore[user_id][route_id].tries += 1;
        unrScore[user_id][route_id].fuelConsumption += fuelConsumed;
        if (unrScore[user_id][route_id].tries > 0) {
            uint myScore = unrScore[user_id][route_id].fuelConsumption/unrScore[user_id][route_id].tries;
            if (!winners[route_id].exists || myScore < winners[route_id].score) {
                winners[route_id].user_id = user_id;
                winners[route_id].score = myScore;
                winners[route_id].exists = true;
                emit WinnerEvent(user_id, myScore);
            }
        }
        emit DriveEvent(user_id, route_id, fuelConsumed);
    }
    
    function addRoute(string memory name, string memory startPosition, string memory endPosition) public {
        Route memory r;
        r.id = totalRoutes; r.name = name; r.startPosition = startPosition; r.endPosition = endPosition; r.users = new uint[](totalUsers);
        routes[totalRoutes++] = r;
        emit RouteEvent(r.id, name, startPosition, endPosition);
    }
    
    function addUser(string memory name, address wallet_address) public {
        User memory u; 
        u.id = totalUsers; u.name = name; u.wallet_address = wallet_address; u.routes = new uint[](totalRoutes);
        users[totalUsers++] = u;
        emit UserEvent(u.id, name, wallet_address);
    }
    
    function subscribe(uint user_id, uint route_id) public {
        users[user_id].routes.push(route_id);
        routes[route_id].users.push(user_id);
        Score memory s; s.tries = 0; s.fuelConsumption = 0;
        unrScore[user_id][route_id] = s;
        emit SubscribeEvent(user_id, route_id);
    }
    
    function totalRecall() private {
        for (uint i = 0; i < totalRoutes; i++) {
            if (winners[i].exists) {
                transfer(users[winners[i].user_id].wallet_address, prize);
                winners[i].exists = false;
            }
            for (uint j = 0; j < totalUsers; j++) {
                unrScore[j][i].tries = 0;
            }
        }
    }
    
    function getScore(uint user_id, uint route_id) public {
        emit ScoreEvent(user_id, route_id, unrScore[user_id][route_id].fuelConsumption/unrScore[user_id][route_id].tries);
    }
    
}