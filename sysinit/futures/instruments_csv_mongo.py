"""
Populate a mongo DB collection with instrument data from a csv

NOTE: THIS DIFFERS FROM 'INSTRUMENTS_CSV_MONGO' AS IT USES THE CONFIG FILE IN  'sysinit.futures.config' rather than the default
 in 'data...'
"""

from sysdata.mongodb.mongo_futures_instruments import mongoFuturesInstrumentData
from sysdata.csv.csv_instrument_config import csvFuturesInstrumentData

INSTRUMENT_CONFIG_PATH = "sysinit.futures.config"

data_out = mongoFuturesInstrumentData()
data_in = csvFuturesInstrumentData(config_path=INSTRUMENT_CONFIG_PATH)
print(data_in)
instrument_list = data_in.get_list_of_instruments()

for instrument_code in instrument_list:
    instrument_object = data_in.get_instrument_data(instrument_code)
    data_out.delete_instrument_data(instrument_code, are_you_sure=True)
    data_out.add_instrument_data(instrument_object)

    # check
    instrument_added = data_out.get_instrument_data(instrument_code)
    print("Added %s to %s" % (instrument_added.instrument_code, data_out))
