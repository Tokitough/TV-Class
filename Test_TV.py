from TV_Class import TV

def main():
    
    # Create tv1
    tv1 = TV()
    tv1.set_channel(30)
    tv1.set_volume(3)
    
    # Create tv2
    tv2 = TV()
    tv2.set_channel(3)
    tv2.set_volume(2)
    
    # Print output
    print("tv1's channel is" , tv1.get_channel() , "and the volume level is" , tv1.get_volume() )
    print("tv2's channel is" , tv2.get_channel() , "and the volume level is" , tv2.get_volume() )
    
main()