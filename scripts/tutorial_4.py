import opensim as osim

# Add the directory containing the geometry files to the OpenSim search paths
osim.ModelVisualizer.addDirToGeometrySearchPaths("/data/Geometry")

xsens_settings = osim.XsensDataReaderSettings('/data/tutorial_4/myIMUMappings.xml')
xsens_reader = osim.XsensDataReader(xsens_settings)

tables = xsens_reader.read('/data/tutorial_4/IMUData/')
quaternion_table = xsens_reader.getOrientationsTable(tables)
osim.STOFileAdapterQuaternion.write(quaternion_table, f'/data/tutorial_4/{xsens_settings.get_trial_prefix()}_orientations.sto')

imu_placer = osim.IMUPlacer('/data/tutorial_4/myIMUPlacer_Setup.xml')
imu_placer.run()

imu_ik_tool = osim.IMUInverseKinematicsTool('/data/tutorial_4/myIMUIK_Setup.xml')
imu_ik_tool.run()
