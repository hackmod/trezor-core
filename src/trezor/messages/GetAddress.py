# Automatically generated by pb2py
from protobuf import protobuf as p
from .MultisigRedeemScriptType import MultisigRedeemScriptType
t = p.MessageType()
t.add_field(1, 'address_n', p.UVarintType, flags=p.FLAG_REPEATED)
t.add_field(2, 'coin_name', p.UnicodeType, default=u'Bitcoin')
t.add_field(3, 'show_display', p.BoolType)
t.add_field(4, 'multisig', p.EmbeddedMessage(MultisigRedeemScriptType))
GetAddress = t
TYPE = const(29)