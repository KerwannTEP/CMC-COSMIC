from cosmic.sample import InitialCMCTable

Singles, Binaries = InitialCMCTable.sampler('cmc', binfrac_model=0.2, primary_model='kroupa01', ecc_model='sana12', porb_model='sana12', cluster_profile='plummer', met=0.014, size=20000, params='Params.ini', gamma=4, r_max=100)

InitialCMCTable.write(Singles, Binaries, filename="input.hdf5")

InitialCMCTable.write(Singles, Binaries, filename="input.fits")
