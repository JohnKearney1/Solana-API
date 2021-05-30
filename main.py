from flask import Flask
from flask_restful import Api, Resource
from pysolana import api as sol

# RESTFUL API INIT
app = Flask(__name__)
rest = Api(app)


# https://docs.solana.com/developing/clients/jsonrpc-api#getaccountinfo ✔ Tested
class getAccountInfo(Resource):

    def get(self, account, chain):
        return sol.getAccountInfo(account, chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getbalance ✔ Tested
class getBalance(Resource):

    def get(self, account):
        return sol.getBalance(account)


# https://docs.solana.com/developing/clients/jsonrpc-api#getblockcommitment ✔ Tested
class getBlockCommitment(Resource):

    def get(self, slot):
        return sol.getBlockCommitment(slot)


# https://docs.solana.com/developing/clients/jsonrpc-api#getblocktime ✔ Tested
class getBlockTime(Resource):

    def get(self, slot):
        return sol.getBlockTime(slot)


# https://docs.solana.com/developing/clients/jsonrpc-api#getclusternodes ✔ Tested
class getClusterNodes(Resource):

    def get(self, chain):
        return sol.getClusterNodes(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getconfirmedblock ✔ Tested
class getConfirmedBlock(Resource):

    def get(self, slot):
        return sol.getConfirmedBlock(slot)


# https://docs.solana.com/developing/clients/jsonrpc-api#getconfirmedblocks ✔ Tested
class getConfirmedBlocks(Resource):

    def get(self, start_slot):
        return sol.getConfirmedBlocks(start_slot)


# https://docs.solana.com/developing/clients/jsonrpc-api#getconfirmedsignaturesforaddress ✔ Tested
class getConfirmedSignaturesForAddress(Resource):

    def get(self, pubkey, start_slot, end_slot):
        return sol.getConfirmedSignaturesForAddress(pubkey, start_slot, end_slot)


# https://docs.solana.com/developing/clients/jsonrpc-api#getconfirmedtransaction ✔ Tested
class getConfirmedTransaction(Resource):

    def get(self, signature, chain):
        return sol.getConfirmedTransaction(signature, chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getepochinfo ✔ Tested
class getEpochInfo(Resource):

    def get(self, chain):

        return sol.getEpochInfo(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getepochschedule ✔ Tested
class getEpochSchedule(Resource):

    def get(self, chain):
        return sol.getEpochSchedule(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getfeecalculatorforblockhash ✔ Tested
class getFeeCalculatorForBlockhash(Resource):

    def get(self, blockhash, chain):
        return sol.getFeeCalculatorForBlockhash(blockhash, chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getfeerategovernor ✔ Tested
class getFeeRateGovernor(Resource):

    def get(self, chain):
        return sol.getFeeRateGovernor(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getfirstavailableblock ✔ Tested
class getFirstAvailableBlock(Resource):

    def get(self, chain):

        return sol.getFirstAvailableBlock(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getgenesishash ✔ Tested
class getGenesisHash(Resource):

    def get(self, chain):
        genesis_hash = sol.getGenesisHash(chain)

        return genesis_hash


# https://docs.solana.com/developing/clients/jsonrpc-api#getidentity ✔ Tested
class getIdentity(Resource):

    def get(self, chain):
        return sol.getIdentity(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getlargestaccounts ✔ Tested
class getLargestAccounts(Resource):

    def get(self, chain):
        return sol.getLargestAccounts(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getleaderschedule ✔ Tested
class getLeaderSchedule(Resource):

    def get(self, slot, chain):
        return sol.getLeaderSchedule(slot, chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getminimumbalanceforrentexemption ✔ Tested
class getMinimumBalanceForRentExemption(Resource):

    def get(self, size, chain):
        return sol.getMinimumBalanceForRentExemption(size, chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getprogramaccounts ✔ Tested
class getProgramAccounts(Resource):

    def get(self, pubkey, chain):
        return sol.getProgramAccounts(pubkey, chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getrecentblockhash ✔ Tested
class getRecentBlockhash(Resource):

    def get(self, chain):
        return sol.getRecentBlockhash(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getsignaturestatuses ✔ Tested
class getSignatureStatuses(Resource):

    def get(self, signature, chain):
        return sol.getSignatureStatuses(signature, chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getslot ✔ Tested
class getSlot(Resource):

    def get(self, chain):
        return sol.getSlot(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getslotleader ✔ Tested
class getSlotLeader(Resource):

    def get(self, chain):
        return sol.getSlotLeader(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#gettotalsupply ✔ Tested
class getTotalSupply(Resource):

    def get(self, chain):
        return sol.getTotalSupply(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#gettransactioncount ✔ Tested
class getTransactionCount(Resource):

    def get(self, chain):
        return sol.getTransactionCount(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getversion ✔ Tested
class getVersion(Resource):

    def get(self, chain):
        return sol.getVersion(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#getvoteaccounts ✔ Tested
class getVoteAccounts(Resource):

    def get(self, chain):
        return sol.getVoteAccounts(chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#requestairdrop ✔ Tested
class requestAirdrop(Resource):

    def get(self, pubkey, lamports, chain):
        return sol.requestAirdrop(pubkey, lamports, chain)


# https://docs.solana.com/developing/clients/jsonrpc-api#sendtransaction ✔ Tested
class sendTransaction(Resource):

    def get(self, signedtx, chain):
        return sol.sendTransaction(signedtx, chain)


# This is the handler section for the resources, and defines where the methods are accessible from on the frontend
rest.add_resource(getBalance, "/balance/<string:account>")
rest.add_resource(getAccountInfo, "/accountInfo/<string:account>&<string:chain>")
rest.add_resource(getBlockCommitment, "/blockCommitment/<int:slot>")
rest.add_resource(getBlockTime, "/blockTime/<int:slot>")
rest.add_resource(getClusterNodes, "/clusterNodes/<string:chain>")
rest.add_resource(getConfirmedBlock, "/confirmedBlock/<int:slot>")
rest.add_resource(getConfirmedBlocks, "/confirmedBlocks/<int:start_slot>")
rest.add_resource(getConfirmedSignaturesForAddress,
                  "/confirmedSignatures/<string:pubkey>&<int:start_slot>&<int:end_slot>")
rest.add_resource(getConfirmedTransaction, "/confirmedTransaction/<string:signature>&<string:chain>")
rest.add_resource(getEpochInfo, "/epochInfo/<string:chain>")
rest.add_resource(getEpochSchedule, "/epochSchedule/<string:chain>")
rest.add_resource(getFeeCalculatorForBlockhash, "/feeCalculator/<string:blockhash>&<string:chain>")
rest.add_resource(getFeeRateGovernor, "/feeGovernor/<string:chain>")
rest.add_resource(getFirstAvailableBlock, "/firstBlock/<string:chain>")
rest.add_resource(getGenesisHash, "/genesisHash/<string:chain>")
rest.add_resource(getIdentity, "/identity/<string:chain>")
rest.add_resource(getLargestAccounts, "/largestAccounts/<string:chain>")
rest.add_resource(getLeaderSchedule, "/leaderSchedule/<int:slot>&<string:chain>")
rest.add_resource(getMinimumBalanceForRentExemption, "/rentExemption/<int:size>&<string:chain>")
rest.add_resource(getProgramAccounts, "/programAccounts/<string:pubkey>&<string:chain>")
rest.add_resource(getRecentBlockhash, "/recentBlockhash/<string:chain>")
rest.add_resource(getSignatureStatuses, "/signatureStatuses/<string:signature>&<string:chain>")
rest.add_resource(getSlot, "/slot/<string:chain>")
rest.add_resource(getSlotLeader, "/slotLeader/<string:chain>")
rest.add_resource(getTotalSupply, "/totalSupply/<string:chain>")
rest.add_resource(getTransactionCount, "/transactionCount/<string:chain>")
rest.add_resource(getVersion, "/version/<string:chain>")
rest.add_resource(getVoteAccounts, "/voteAccounts/<string:chain>")
rest.add_resource(requestAirdrop, "/airdrop/<string:pubkey>&<int:lamports>&<string:chain>")
rest.add_resource(sendTransaction, "/sendTransaction/<string:signedtx>&<string:chain>")

if __name__ == "__main__":
    app.run(debug=True, port=8042)
